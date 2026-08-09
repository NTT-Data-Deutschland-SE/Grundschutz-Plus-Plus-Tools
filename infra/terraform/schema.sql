-- Schema für das GS++-Datenbank-Backend (PLAN_Datenbank-Backend.md, Phase 1).
-- Version 2: Rechte kommen aus TABELLEN, nicht aus JWT-Claims.
--
-- Warum: Claims leben bis zu einer Stunde im Access-Token — ein entzogenes
-- Recht wirkte erst nach dem nächsten Refresh. Außerdem war der frühere
-- user_metadata-Fallback selbst editierbar (PUT /auth/v1/user), also eine
-- Privilege Escalation. Jetzt gilt: ohne Zeile in public.memberships kein
-- Zugriff, und Änderungen des Admins greifen mit der nächsten Anfrage.
--
-- ACHTUNG beim Einspielen auf einen Bestand mit Version 1: die Testbenutzer
-- brauchen anschließend Zeilen in memberships (macht seed_users.sh bzw. das
-- Startskript für den Admin) — vorher sehen sie NICHTS mehr. Das ist kein
-- Unfall, sondern die Durchsetzung.
--
-- Idempotent: mehrfaches Einspielen ist vorgesehen (IF NOT EXISTS, OR REPLACE,
-- DROP POLICY IF EXISTS).

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ============================================================ Tabellen

CREATE TABLE IF NOT EXISTS public.orgs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

INSERT INTO public.orgs (id, name)
VALUES ('00000000-0000-0000-0000-000000000001', 'Default Org')
ON CONFLICT (id) DO NOTHING;

-- Globale Rolle je Benutzer und Org. DIE Quelle der Wahrheit für Rechte.
CREATE TABLE IF NOT EXISTS public.memberships (
  user_id uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  org_id uuid NOT NULL REFERENCES public.orgs(id) ON DELETE CASCADE,
  gpp_role text NOT NULL CHECK (gpp_role IN ('leser', 'bearbeiter', 'pruefer', 'admin')),
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, org_id)
);

-- Abweichende Rolle je Set (vom Admin vergeben). Ohne Eintrag gilt die
-- globale Rolle; 'admin' ist bewusst nicht je Set vergebbar.
CREATE TABLE IF NOT EXISTS public.set_permissions (
  user_id uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  org uuid NOT NULL REFERENCES public.orgs(id) ON DELETE CASCADE,
  set_name text NOT NULL,
  gpp_role text NOT NULL CHECK (gpp_role IN ('leser', 'bearbeiter', 'pruefer')),
  granted_by uuid,
  granted_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, org, set_name)
);

CREATE TABLE IF NOT EXISTS public.artefacts (
  id text PRIMARY KEY,
  set_name text NOT NULL DEFAULT 'standard',
  stage text NOT NULL,
  kind text NOT NULL,
  title text NOT NULL,
  filename text NOT NULL,
  tool text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now(),
  size integer NOT NULL DEFAULT 0,
  sha256 text NOT NULL,
  meta jsonb NOT NULL DEFAULT '{}'::jsonb,
  data jsonb NOT NULL DEFAULT '{}'::jsonb,
  org uuid NOT NULL DEFAULT '00000000-0000-0000-0000-000000000001'::uuid,
  updated_by uuid
);

CREATE INDEX IF NOT EXISTS idx_artefacts_set_org ON public.artefacts(set_name, org);

CREATE TABLE IF NOT EXISTS public.set_locks (
  set_name text NOT NULL,
  org uuid NOT NULL DEFAULT '00000000-0000-0000-0000-000000000001'::uuid,
  holder uuid NOT NULL,
  holder_name text NOT NULL,
  acquired_at timestamptz NOT NULL DEFAULT now(),
  heartbeat_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (set_name, org)
);

CREATE TABLE IF NOT EXISTS public.audit (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  action text NOT NULL,
  entity_type text NOT NULL,
  entity_id text,
  user_id uuid,
  org uuid,
  details jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

-- ============================================================ Rollen-Auflösung

-- Org des Anfragenden — aus memberships, nicht aus Claims.
CREATE OR REPLACE FUNCTION public.auth_org() RETURNS uuid
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT org_id FROM public.memberships WHERE user_id = auth.uid() LIMIT 1;
$$;

-- Globale Rolle. KEIN Fallback auf 'leser' mehr: wer keine Mitgliedschaft
-- hat, hat keine Rolle und sieht nichts.
CREATE OR REPLACE FUNCTION public.auth_gpp_role() RETURNS text
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT gpp_role FROM public.memberships WHERE user_id = auth.uid() LIMIT 1;
$$;

-- Wirksame Rolle auf einem Set: Set-Eintrag schlägt globale Rolle;
-- ein globaler admin lässt sich per Set-Eintrag nicht herabstufen.
CREATE OR REPLACE FUNCTION public.gpp_set_role(p_set_name text) RETURNS text
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT CASE WHEN m.gpp_role = 'admin' THEN 'admin'
              ELSE COALESCE(sp.gpp_role, m.gpp_role) END
  FROM public.memberships m
  LEFT JOIN public.set_permissions sp
    ON sp.user_id = m.user_id AND sp.org = m.org_id AND sp.set_name = p_set_name
  WHERE m.user_id = auth.uid()
  LIMIT 1;
$$;

-- Schreibrecht nach Plan §4: bearbeiter alles außer ap/ar; pruefer nur
-- ap/ar/poam; admin alles; leser nichts.
CREATE OR REPLACE FUNCTION public.gpp_can_write(p_set_name text, p_kind text) RETURNS boolean
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT CASE public.gpp_set_role(p_set_name)
    WHEN 'admin'      THEN true
    WHEN 'bearbeiter' THEN p_kind NOT IN ('ap', 'ar')
    WHEN 'pruefer'    THEN p_kind IN ('ap', 'ar', 'poam')
    ELSE false
  END;
$$;

-- ============================================================ RLS

ALTER TABLE public.artefacts       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.set_locks       ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orgs            ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.memberships     ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.set_permissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.audit           ENABLE ROW LEVEL SECURITY;

-- Alte v1-Policies räumen (Namen aus der ersten Fassung).
DROP POLICY IF EXISTS "Allow read artefacts for authenticated users" ON public.artefacts;
DROP POLICY IF EXISTS "Allow write artefacts for bearbeiter, pruefer, admin" ON public.artefacts;
DROP POLICY IF EXISTS "Allow read locks for authenticated users" ON public.set_locks;
DROP POLICY IF EXISTS "Allow modify locks for authenticated users" ON public.set_locks;

-- Artefakte: Lesen für jedes Org-Mitglied, Schreiben nach wirksamer Set-Rolle
-- und kind. Getrennte Policies je Verb, damit ein DELETE über einen
-- set_name-Filter nur die Zeilen trifft, die die Rolle hergibt.
DROP POLICY IF EXISTS artefacts_select ON public.artefacts;
CREATE POLICY artefacts_select ON public.artefacts FOR SELECT TO authenticated
  USING (org = public.auth_org());

DROP POLICY IF EXISTS artefacts_insert ON public.artefacts;
CREATE POLICY artefacts_insert ON public.artefacts FOR INSERT TO authenticated
  WITH CHECK (org = public.auth_org() AND public.gpp_can_write(set_name, kind));

DROP POLICY IF EXISTS artefacts_update ON public.artefacts;
CREATE POLICY artefacts_update ON public.artefacts FOR UPDATE TO authenticated
  USING (org = public.auth_org() AND public.gpp_can_write(set_name, kind))
  WITH CHECK (org = public.auth_org() AND public.gpp_can_write(set_name, kind));

DROP POLICY IF EXISTS artefacts_delete ON public.artefacts;
CREATE POLICY artefacts_delete ON public.artefacts FOR DELETE TO authenticated
  USING (org = public.auth_org() AND public.gpp_can_write(set_name, kind));

-- Sperren: Lesen für Mitglieder; Erwerb läuft über die RPC (SECURITY DEFINER,
-- prüft selbst); direktes Löschen nur Halter oder admin — der Plan reserviert
-- das Brechen fremder Sperren für admin.
DROP POLICY IF EXISTS set_locks_select ON public.set_locks;
CREATE POLICY set_locks_select ON public.set_locks FOR SELECT TO authenticated
  USING (org = public.auth_org());

DROP POLICY IF EXISTS set_locks_delete ON public.set_locks;
CREATE POLICY set_locks_delete ON public.set_locks FOR DELETE TO authenticated
  USING (org = public.auth_org() AND (holder = auth.uid() OR public.auth_gpp_role() = 'admin'));

-- Mitgliedschaften und Set-Rechte: jeder sieht die eigenen, admin alle der
-- Org. Geändert wird ausschließlich über die admin_*-RPCs.
DROP POLICY IF EXISTS memberships_select ON public.memberships;
CREATE POLICY memberships_select ON public.memberships FOR SELECT TO authenticated
  USING (user_id = auth.uid() OR (org_id = public.auth_org() AND public.auth_gpp_role() = 'admin'));

DROP POLICY IF EXISTS set_permissions_select ON public.set_permissions;
CREATE POLICY set_permissions_select ON public.set_permissions FOR SELECT TO authenticated
  USING (user_id = auth.uid() OR (org = public.auth_org() AND public.auth_gpp_role() = 'admin'));

DROP POLICY IF EXISTS orgs_select ON public.orgs;
CREATE POLICY orgs_select ON public.orgs FOR SELECT TO authenticated
  USING (id = public.auth_org());

-- Audit: nur admin liest; geschrieben wird per Trigger (SECURITY DEFINER).
DROP POLICY IF EXISTS audit_select ON public.audit;
CREATE POLICY audit_select ON public.audit FOR SELECT TO authenticated
  USING (org = public.auth_org() AND public.auth_gpp_role() = 'admin');

-- ============================================================ Trigger

-- org und updated_by setzt der Server aus der Sitzung — was der Client
-- schickt, wird überschrieben. Zeitstempel bleiben Client-Sache: die lokale
-- Änderungszeit ist die fachlich richtige.
CREATE OR REPLACE FUNCTION public.artefacts_stamp() RETURNS trigger
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  NEW.org := COALESCE(public.auth_org(), NEW.org);
  NEW.updated_by := COALESCE(auth.uid(), NEW.updated_by);
  RETURN NEW;
END;
$$;
DROP TRIGGER IF EXISTS trg_artefacts_stamp ON public.artefacts;
CREATE TRIGGER trg_artefacts_stamp BEFORE INSERT OR UPDATE ON public.artefacts
  FOR EACH ROW EXECUTE FUNCTION public.artefacts_stamp();

-- Jede Schreiboperation erzeugt eine audit-Zeile (Plan Phase 1). Bewusst ohne
-- data-Inhalt — der Prüfpfad braucht Wer/Was/Wann, nicht das Dokument.
CREATE OR REPLACE FUNCTION public.audit_row() RETURNS trigger
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  IF TG_TABLE_NAME = 'artefacts' THEN
    INSERT INTO public.audit (action, entity_type, entity_id, user_id, org, details)
    VALUES (
      lower(TG_OP), TG_TABLE_NAME, COALESCE(NEW.id, OLD.id),
      auth.uid(), public.auth_org(),
      jsonb_build_object('set', COALESCE(NEW.set_name, OLD.set_name), 'kind', COALESCE(NEW.kind, OLD.kind), 'sha256', COALESCE(NEW.sha256, OLD.sha256))
    );
  ELSE
    INSERT INTO public.audit (action, entity_type, entity_id, user_id, org, details)
    VALUES (
      lower(TG_OP), TG_TABLE_NAME, NULL,
      auth.uid(), public.auth_org(),
      to_jsonb(COALESCE(NEW, OLD)) - 'data'
    );
  END IF;
  RETURN COALESCE(NEW, OLD);
END;
$$;
DROP TRIGGER IF EXISTS trg_audit_artefacts ON public.artefacts;
CREATE TRIGGER trg_audit_artefacts AFTER INSERT OR UPDATE OR DELETE ON public.artefacts
  FOR EACH ROW EXECUTE FUNCTION public.audit_row();
DROP TRIGGER IF EXISTS trg_audit_set_locks ON public.set_locks;
CREATE TRIGGER trg_audit_set_locks AFTER INSERT OR UPDATE OR DELETE ON public.set_locks
  FOR EACH ROW EXECUTE FUNCTION public.audit_row();
DROP TRIGGER IF EXISTS trg_audit_memberships ON public.memberships;
CREATE TRIGGER trg_audit_memberships AFTER INSERT OR UPDATE OR DELETE ON public.memberships
  FOR EACH ROW EXECUTE FUNCTION public.audit_row();
DROP TRIGGER IF EXISTS trg_audit_set_permissions ON public.set_permissions;
CREATE TRIGGER trg_audit_set_permissions AFTER INSERT OR UPDATE OR DELETE ON public.set_permissions
  FOR EACH ROW EXECUTE FUNCTION public.audit_row();

-- ============================================================ RPCs

-- Sperr-Erwerb, atomar; erneuter Aufruf des Halters = Heartbeat; abgelaufene
-- Sperren (5 min ohne Heartbeat) werden übernommen. Leeres Ergebnis heißt:
-- jemand anderes hält sie. Sperren dürfen bearbeiter und admin (Plan §4).
CREATE OR REPLACE FUNCTION public.acquire_set_lock(p_set_name text, p_holder_name text)
RETURNS SETOF public.set_locks
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
DECLARE
  v_org uuid := public.auth_org();
BEGIN
  IF v_org IS NULL OR public.gpp_set_role(p_set_name) NOT IN ('bearbeiter', 'admin') THEN
    RAISE EXCEPTION 'keine Berechtigung, dieses Set zu sperren';
  END IF;
  RETURN QUERY
  INSERT INTO public.set_locks (set_name, org, holder, holder_name, acquired_at, heartbeat_at)
  VALUES (p_set_name, v_org, auth.uid(), p_holder_name, now(), now())
  ON CONFLICT (set_name, org) DO UPDATE
     SET holder = EXCLUDED.holder,
         holder_name = EXCLUDED.holder_name,
         acquired_at = now(),
         heartbeat_at = now()
   WHERE set_locks.holder = EXCLUDED.holder
      OR set_locks.heartbeat_at < now() - INTERVAL '5 minutes'
  RETURNING *;
END;
$$;

-- Wer bin ich, was darf ich — eine Anfrage für die UI. Die Durchsetzung
-- passiert in den Policies; das hier ist nur Anzeige.
CREATE OR REPLACE FUNCTION public.whoami() RETURNS jsonb
LANGUAGE sql STABLE SECURITY DEFINER SET search_path = public AS $$
  SELECT jsonb_build_object(
    'user_id', auth.uid(),
    'email', (SELECT email FROM auth.users WHERE id = auth.uid()),
    'org', public.auth_org(),
    'gpp_role', public.auth_gpp_role(),
    'set_roles', COALESCE((SELECT jsonb_object_agg(set_name, gpp_role)
                             FROM public.set_permissions WHERE user_id = auth.uid()), '{}'::jsonb)
  );
$$;

-- ---------- Benutzerverwaltung (nur admin; config.html ruft diese RPCs) ----

CREATE OR REPLACE FUNCTION public.gpp_require_admin() RETURNS void
LANGUAGE plpgsql STABLE SECURITY DEFINER SET search_path = public AS $$
BEGIN
  IF public.auth_gpp_role() IS DISTINCT FROM 'admin' THEN
    RAISE EXCEPTION 'nur admin';
  END IF;
END;
$$;

CREATE OR REPLACE FUNCTION public.admin_list_users()
RETURNS TABLE (user_id uuid, email text, gpp_role text, set_roles jsonb,
               created_at timestamptz, last_sign_in_at timestamptz)
LANGUAGE plpgsql STABLE SECURITY DEFINER SET search_path = public AS $$
BEGIN
  PERFORM public.gpp_require_admin();
  RETURN QUERY
  SELECT u.id, u.email::text, m.gpp_role,
         COALESCE((SELECT jsonb_object_agg(sp.set_name, sp.gpp_role)
                     FROM public.set_permissions sp
                    WHERE sp.user_id = u.id AND sp.org = public.auth_org()), '{}'::jsonb),
         u.created_at, u.last_sign_in_at
    FROM auth.users u
    JOIN public.memberships m ON m.user_id = u.id AND m.org_id = public.auth_org()
   ORDER BY u.email;
END;
$$;

-- Legt Konto UND Mitgliedschaft an. Direkt in auth.users/auth.identities —
-- der pragmatische Weg für den Test-Stack, weil der Browser-Client den
-- SERVICE_ROLE_KEY nie sehen darf und GoTrues Admin-API genau den verlangt.
-- Produktiv gehört hier die GoTrue-Admin-API hin (siehe seed_users.sh).
CREATE OR REPLACE FUNCTION public.admin_create_user(p_email text, p_password text, p_gpp_role text)
RETURNS jsonb
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public, extensions AS $$
DECLARE
  v_id uuid := gen_random_uuid();
BEGIN
  PERFORM public.gpp_require_admin();
  IF p_gpp_role NOT IN ('leser', 'bearbeiter', 'pruefer', 'admin') THEN
    RAISE EXCEPTION 'unbekannte Rolle %', p_gpp_role;
  END IF;
  IF length(coalesce(p_password, '')) < 10 THEN
    RAISE EXCEPTION 'Passwort zu kurz (mindestens 10 Zeichen)';
  END IF;
  IF EXISTS (SELECT 1 FROM auth.users WHERE lower(email) = lower(p_email)) THEN
    RAISE EXCEPTION 'Konto % existiert bereits', p_email;
  END IF;

  INSERT INTO auth.users (instance_id, id, aud, role, email, encrypted_password,
    email_confirmed_at, raw_app_meta_data, raw_user_meta_data, created_at, updated_at,
    confirmation_token, recovery_token, email_change_token_new, email_change)
  VALUES ('00000000-0000-0000-0000-000000000000', v_id, 'authenticated', 'authenticated',
    lower(p_email), extensions.crypt(p_password, extensions.gen_salt('bf')),
    now(), jsonb_build_object('provider', 'email', 'providers', jsonb_build_array('email')),
    '{}'::jsonb, now(), now(), '', '', '', '');

  INSERT INTO auth.identities (id, user_id, provider_id, identity_data, provider,
    last_sign_in_at, created_at, updated_at)
  VALUES (gen_random_uuid(), v_id, v_id::text,
    jsonb_build_object('sub', v_id::text, 'email', lower(p_email), 'email_verified', true),
    'email', now(), now(), now());

  INSERT INTO public.memberships (user_id, org_id, gpp_role)
  VALUES (v_id, public.auth_org(), p_gpp_role);

  RETURN jsonb_build_object('user_id', v_id, 'email', lower(p_email), 'gpp_role', p_gpp_role);
END;
$$;

CREATE OR REPLACE FUNCTION public.admin_delete_user(p_user_id uuid) RETURNS void
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  PERFORM public.gpp_require_admin();
  IF p_user_id = auth.uid() THEN
    RAISE EXCEPTION 'das eigene Konto löscht man nicht aus Versehen';
  END IF;
  IF NOT EXISTS (SELECT 1 FROM public.memberships
                  WHERE user_id = p_user_id AND org_id = public.auth_org()) THEN
    RAISE EXCEPTION 'kein Mitglied dieser Organisation';
  END IF;
  -- memberships/set_permissions räumen die FKs (ON DELETE CASCADE) ab.
  DELETE FROM auth.users WHERE id = p_user_id;
END;
$$;

CREATE OR REPLACE FUNCTION public.admin_set_role(p_user_id uuid, p_gpp_role text) RETURNS void
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  PERFORM public.gpp_require_admin();
  IF p_gpp_role NOT IN ('leser', 'bearbeiter', 'pruefer', 'admin') THEN
    RAISE EXCEPTION 'unbekannte Rolle %', p_gpp_role;
  END IF;
  IF p_user_id = auth.uid() AND p_gpp_role <> 'admin' THEN
    RAISE EXCEPTION 'die eigene admin-Rolle gibt man nicht selbst ab — ein zweiter admin muss das tun';
  END IF;
  INSERT INTO public.memberships (user_id, org_id, gpp_role)
  VALUES (p_user_id, public.auth_org(), p_gpp_role)
  ON CONFLICT (user_id, org_id) DO UPDATE SET gpp_role = EXCLUDED.gpp_role;
END;
$$;

CREATE OR REPLACE FUNCTION public.admin_set_set_role(p_user_id uuid, p_set_name text, p_gpp_role text)
RETURNS void
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  PERFORM public.gpp_require_admin();
  IF p_gpp_role NOT IN ('leser', 'bearbeiter', 'pruefer') THEN
    RAISE EXCEPTION 'je Set sind nur leser, bearbeiter, pruefer vergebbar';
  END IF;
  INSERT INTO public.set_permissions (user_id, org, set_name, gpp_role, granted_by)
  VALUES (p_user_id, public.auth_org(), p_set_name, p_gpp_role, auth.uid())
  ON CONFLICT (user_id, org, set_name) DO UPDATE
    SET gpp_role = EXCLUDED.gpp_role, granted_by = EXCLUDED.granted_by, granted_at = now();
END;
$$;

CREATE OR REPLACE FUNCTION public.admin_clear_set_role(p_user_id uuid, p_set_name text) RETURNS void
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
BEGIN
  PERFORM public.gpp_require_admin();
  DELETE FROM public.set_permissions
   WHERE user_id = p_user_id AND org = public.auth_org() AND set_name = p_set_name;
END;
$$;

-- ============================================================ Grants

-- Kein anon auf den Tabellen mehr: ohne Anmeldung gibt es nichts zu sehen.
REVOKE ALL ON public.artefacts, public.set_locks, public.orgs,
           public.memberships, public.set_permissions, public.audit FROM anon;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.artefacts  TO authenticated, service_role;
GRANT SELECT, DELETE                 ON public.set_locks  TO authenticated, service_role;
GRANT SELECT ON public.orgs, public.memberships, public.set_permissions, public.audit
  TO authenticated, service_role;
GRANT INSERT, UPDATE, DELETE ON public.memberships, public.set_permissions
  TO service_role;   -- seed_users.sh über PostgREST; Clients laufen über die RPCs

GRANT EXECUTE ON FUNCTION public.acquire_set_lock, public.whoami,
  public.admin_list_users, public.admin_create_user, public.admin_delete_user,
  public.admin_set_role, public.admin_set_set_role, public.admin_clear_set_role
  TO authenticated, service_role;
