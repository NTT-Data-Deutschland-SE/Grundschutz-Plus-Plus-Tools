# Zeichensatz bewusst ohne Sonderzeichen: die Werte laufen im Startskript durch
# sed und landen in Verbindungs-URLs. Die Entropie holt die Länge.
resource "random_password" "postgres" {
  length  = 40
  special = false
}

resource "random_password" "jwt_secret" {
  length  = 64
  special = false
}

resource "random_password" "dashboard" {
  length  = 32
  special = false
}

# Erstes Konto der Anwendung (Rolle admin) — legt Benutzer an und vergibt
# Rechte, wie es der Plan für Pfad A vorsieht. Angelegt wird es vom
# Startskript, sobald der Stack läuft; das Passwort liegt nur im Secret
# Manager und im State.
resource "random_password" "admin" {
  length  = 24
  special = false
}

locals {
  secrets = {
    postgres-password  = random_password.postgres.result
    jwt-secret         = random_password.jwt_secret.result
    dashboard-password = random_password.dashboard.result
    admin-password     = random_password.admin.result
  }
}

resource "google_secret_manager_secret" "this" {
  for_each = local.secrets

  secret_id = "${var.name_prefix}-${each.key}"

  replication {
    user_managed {
      replicas {
        location = var.region
      }
    }
  }

  depends_on = [google_project_service.required]
}

resource "google_secret_manager_secret_version" "this" {
  for_each = local.secrets

  secret      = google_secret_manager_secret.this[each.key].id
  secret_data = each.value
}

resource "google_service_account" "vm" {
  account_id   = "${var.name_prefix}-supabase-vm"
  display_name = "GS++ Supabase-Testinstanz"
}

# Nur Lesezugriff auf genau diese drei Secrets — kein projektweites
# secretAccessor.
resource "google_secret_manager_secret_iam_member" "vm" {
  for_each = google_secret_manager_secret.this

  secret_id = each.value.id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${google_service_account.vm.email}"
}

resource "google_project_iam_member" "vm" {
  for_each = toset([
    "roles/logging.logWriter",
    "roles/monitoring.metricWriter",
  ])

  project = var.project_id
  role    = each.value
  member  = "serviceAccount:${google_service_account.vm.email}"
}
