-- Schema Definition for Grundschutz++ (GS++) Supabase Backend

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Helper Functions for JWT extraction
CREATE OR REPLACE FUNCTION auth_org() RETURNS uuid AS $$
BEGIN
  RETURN NULLIF(
    COALESCE(
      current_setting('request.jwt.claims', true)::jsonb -> 'app_metadata' ->> 'org',
      current_setting('request.jwt.claims', true)::jsonb -> 'user_metadata' ->> 'org',
      current_setting('request.jwt.claims', true)::jsonb ->> 'org'
    ), ''
  )::uuid;
END;
$$ LANGUAGE plpgsql STABLE;

CREATE OR REPLACE FUNCTION auth_gpp_role() RETURNS text AS $$
BEGIN
  RETURN COALESCE(
    current_setting('request.jwt.claims', true)::jsonb -> 'app_metadata' ->> 'gpp_role',
    current_setting('request.jwt.claims', true)::jsonb -> 'user_metadata' ->> 'gpp_role',
    current_setting('request.jwt.claims', true)::jsonb ->> 'gpp_role',
    'leser'
  );
END;
$$ LANGUAGE plpgsql STABLE;

-- 1. Orgs
CREATE TABLE IF NOT EXISTS public.orgs (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now()
);

-- Default Org for testing
INSERT INTO public.orgs (id, name)
VALUES ('00000000-0000-0000-0000-000000000001', 'Default Org')
ON CONFLICT (id) DO NOTHING;

-- 2. Memberships
CREATE TABLE IF NOT EXISTS public.memberships (
  user_id uuid NOT NULL,
  org_id uuid NOT NULL REFERENCES public.orgs(id) ON DELETE CASCADE,
  gpp_role text NOT NULL CHECK (gpp_role IN ('leser', 'bearbeiter', 'pruefer', 'admin')),
  created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, org_id)
);

-- 3. Artefacts Table
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

-- 4. Locks Table
CREATE TABLE IF NOT EXISTS public.set_locks (
  set_name text NOT NULL,
  org uuid NOT NULL DEFAULT '00000000-0000-0000-0000-000000000001'::uuid,
  holder uuid NOT NULL,
  holder_name text NOT NULL,
  acquired_at timestamptz NOT NULL DEFAULT now(),
  heartbeat_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (set_name, org)
);

-- 5. Audit Log Table
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

-- RLS Enablement
ALTER TABLE public.artefacts ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.set_locks ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.orgs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.memberships ENABLE ROW LEVEL SECURITY;

-- RLS Policies for Artefacts
CREATE POLICY "Allow read artefacts for authenticated users"
ON public.artefacts FOR SELECT
TO authenticated
USING (true);

CREATE POLICY "Allow write artefacts for bearbeiter, pruefer, admin"
ON public.artefacts FOR ALL
TO authenticated
USING (
  auth_gpp_role() IN ('bearbeiter', 'pruefer', 'admin')
)
WITH CHECK (
  auth_gpp_role() IN ('bearbeiter', 'pruefer', 'admin')
);

-- RLS Policies for Locks
CREATE POLICY "Allow read locks for authenticated users"
ON public.set_locks FOR SELECT
TO authenticated
USING (true);

CREATE POLICY "Allow modify locks for authenticated users"
ON public.set_locks FOR ALL
TO authenticated
USING (
  auth_gpp_role() IN ('bearbeiter', 'admin')
)
WITH CHECK (
  auth_gpp_role() IN ('bearbeiter', 'admin')
);

-- RPC for Lock Acquisition
CREATE OR REPLACE FUNCTION acquire_set_lock(p_set_name text, p_holder_name text)
RETURNS SETOF public.set_locks AS $$
DECLARE
  v_org uuid := COALESCE(auth_org(), '00000000-0000-0000-0000-000000000001'::uuid);
  v_user_id uuid := auth.uid();
BEGIN
  RETURN QUERY
  INSERT INTO public.set_locks (set_name, org, holder, holder_name, acquired_at, heartbeat_at)
  VALUES (p_set_name, v_org, v_user_id, p_holder_name, now(), now())
  ON CONFLICT (set_name, org) DO UPDATE
     SET holder = EXCLUDED.holder,
         holder_name = EXCLUDED.holder_name,
         acquired_at = now(),
         heartbeat_at = now()
   WHERE set_locks.holder = EXCLUDED.holder
      OR set_locks.heartbeat_at < now() - INTERVAL '5 minutes'
  RETURNING *;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Grants
GRANT ALL ON public.artefacts TO anon, authenticated, service_role;
GRANT ALL ON public.set_locks TO anon, authenticated, service_role;
GRANT ALL ON public.orgs TO anon, authenticated, service_role;
GRANT ALL ON public.memberships TO anon, authenticated, service_role;
GRANT EXECUTE ON FUNCTION acquire_set_lock TO authenticated, service_role;
