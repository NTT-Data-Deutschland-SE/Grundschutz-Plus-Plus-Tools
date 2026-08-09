variable "project_id" {
  description = "Bestehendes GCP-Projekt, in dem die Testumgebung entsteht."
  type        = string
}

variable "region" {
  description = "Region. Voreinstellung Frankfurt — die Testdaten sind zwar Wegwerfware, aber der Kontext ist BSI."
  type        = string
  default     = "europe-west3"
}

variable "zone" {
  description = "Zone innerhalb der Region."
  type        = string
  default     = "europe-west3-b"
}

variable "name_prefix" {
  description = "Präfix für alle Ressourcennamen."
  type        = string
  default     = "gpp"
}

variable "machine_type" {
  description = <<-EOT
    e2-standard-2 (8 GB) trägt den vollständigen Supabase-Compose-Stack.
    e2-medium (4 GB) reicht nur, wenn analytics/realtime/storage abgeschaltet
    werden — der mitgelieferte Compose-Stand verdrahtet die aber als
    depends_on, deshalb ist Trimmen mehr Arbeit als der Preisunterschied wert.
  EOT
  type        = string
  default     = "e2-standard-2"
}

variable "boot_disk_gb" {
  description = "Größe der Bootplatte in GB (Images, Postgres-Daten und Logs liegen darauf)."
  type        = number
  default     = 50
}

variable "domain" {
  description = <<-EOT
    Vollständiger Hostname, unter dem Caddy die Werkzeuge und die API
    ausliefert, z. B. "gpp-test.example.de". Leer lassen für Phase 1: dann
    bleibt die VM ohne offene Ports und alles läuft durch den IAP-Tunnel.
    Sobald der Browser die DB erreichen soll (Phase 2), wird der Name
    gebraucht — ohne TLS kein fetch() von einer HTTPS-Seite.
  EOT
  type        = string
  default     = ""
}

variable "allowed_cidrs" {
  description = <<-EOT
    Quell-Netze, die 443 erreichen dürfen. Nur relevant, wenn "domain" gesetzt
    ist. Bewusst keine Voreinstellung auf 0.0.0.0/0. Port 80 steht unabhängig
    davon offen — die ACME-Prüfung von Let's Encrypt kommt aus wechselnden
    Netzen und lässt sich nicht sinnvoll einschränken; auf 80 liegt nur die
    Challenge und die Umleitung nach HTTPS.
  EOT
  type        = list(string)
  default     = []

  validation {
    condition     = !contains(var.allowed_cidrs, "0.0.0.0/0")
    error_message = "0.0.0.0/0 ist für eine Testinstanz mit echten Zugangsdaten nicht vorgesehen. Trage die eigene öffentliche IP als /32 ein."
  }
}

variable "dns_managed_zone" {
  description = "Name einer bestehenden Cloud-DNS-Zone im selben Projekt. Leer lassen, wenn der A-Record beim Registrar gepflegt wird."
  type        = string
  default     = ""
}

variable "supabase_ref" {
  description = <<-EOT
    Git-Ref des supabase/supabase-Repos, aus dem das docker/-Verzeichnis
    geholt wird. Grundregel 8 des Projekts (Quellen sind commit-gepinnt) gilt
    auch hier: für alles jenseits eines ersten Versuchs einen Commit-SHA
    eintragen, nicht "master".
  EOT
  type        = string
  default     = "master"
}

variable "admin_email" {
  description = "E-Mail des ersten admin-Kontos der Anwendung. Das Startskript legt es über die GoTrue-Admin-API an; das Passwort kommt aus dem Secret Manager (gpp-admin-password)."
  type        = string
  default     = "admin@example.com"
}

variable "allow_public_api" {
  description = "Freigabe von Port 8000 in der Firewall für direkte API-Anfragen (z.B. durch Test-Agenten)."
  type        = bool
  default     = true
}

variable "seed_test_users" {
  description = "Zusätzliche Testbenutzer (bearbeiter@example.com und leser@example.com) beim Boot automatisch anlegen. Standard ist false (nur Admin-Konto)."
  type        = bool
  default     = false
}

variable "billing_account" {
  description = "Abrechnungskonto-ID für das Budget-Alarm. Leer lassen, wenn keine Rechte darauf bestehen — dann entfällt das Budget."
  type        = string
  default     = ""
}

variable "budget_amount" {
  description = "Monatliches Budget in ganzen Währungseinheiten des Abrechnungskontos."
  type        = number
  default     = 50
}

locals {
  tls_enabled = var.domain != ""
  tag         = "${var.name_prefix}-supabase"
}

# Ein Hostname ohne freigegebene Quell-Netze wäre eine Adresse, die niemand
# erreicht.
resource "terraform_data" "guard_allowed_cidrs" {
  lifecycle {
    precondition {
      condition     = !local.tls_enabled || length(var.allowed_cidrs) > 0
      error_message = "Mit gesetztem \"domain\" muss \"allowed_cidrs\" mindestens ein Netz enthalten, sonst erreicht niemand Port 443."
    }
  }
}
