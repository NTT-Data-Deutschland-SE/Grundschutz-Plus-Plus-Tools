resource "google_project_service" "required" {
  for_each = toset(compact([
    "compute.googleapis.com",
    "iap.googleapis.com",
    "secretmanager.googleapis.com",
    "oslogin.googleapis.com",
    var.dns_managed_zone != "" ? "dns.googleapis.com" : "",
    var.billing_account != "" ? "billingbudgets.googleapis.com" : "",
  ]))

  service = each.value

  # Beim Zerstören der Testumgebung sollen keine APIs im Projekt abgeschaltet
  # werden, die daneben noch jemand nutzt.
  disable_on_destroy = false
}

resource "google_compute_network" "vpc" {
  name                    = "${var.name_prefix}-vpc"
  auto_create_subnetworks = false
  depends_on              = [google_project_service.required]
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.name_prefix}-subnet"
  ip_cidr_range = "10.10.0.0/24"
  region        = var.region
  network       = google_compute_network.vpc.id

  # Damit Verbindungsversuche in den Logs auftauchen, ohne dass ein
  # Flow-Log-Berg entsteht.
  log_config {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

# Der einzige Verwaltungszugang: IAP-TCP-Forwarding aus dem festen Google-Netz.
# 22 für SSH, 5432 für psql-Migrationen durch den Tunnel, 8000 für Kong —
# damit Phase 1 vollständig ohne einen offenen Port abnehmbar ist.
resource "google_compute_firewall" "iap" {
  name          = "${var.name_prefix}-allow-iap"
  network       = google_compute_network.vpc.name
  direction     = "INGRESS"
  source_ranges = ["35.235.240.0/20"]
  target_tags   = [local.tag]

  allow {
    protocol = "tcp"
    ports    = ["22", "5432", "8000"]
  }
}

# Port 80 trägt ausschließlich die ACME-Challenge und die Umleitung nach
# HTTPS. Let's Encrypt prüft aus wechselnden Netzen, eine Einschränkung wäre
# hier nur Kosmetik mit Ausfallrisiko.
resource "google_compute_firewall" "acme" {
  count = local.tls_enabled ? 1 : 0

  name          = "${var.name_prefix}-allow-acme"
  network       = google_compute_network.vpc.name
  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
  target_tags   = [local.tag]

  allow {
    protocol = "tcp"
    ports    = ["80"]
  }
}

resource "google_compute_firewall" "https" {
  count = local.tls_enabled ? 1 : 0

  name          = "${var.name_prefix}-allow-https"
  network       = google_compute_network.vpc.name
  direction     = "INGRESS"
  source_ranges = var.allowed_cidrs
  target_tags   = [local.tag]

  allow {
    protocol = "tcp"
    ports    = ["443"]
  }
}

# Optional: Öffentlicher Zugriff auf Port 8000 für API-Tests durch externe Agenten
resource "google_compute_firewall" "public_api" {
  count = var.allow_public_api ? 1 : 0

  name          = "${var.name_prefix}-allow-kong-external"
  network       = google_compute_network.vpc.name
  direction     = "INGRESS"
  source_ranges = ["0.0.0.0/0"]
  target_tags   = [local.tag]

  allow {
    protocol = "tcp"
    ports    = ["8000"]
  }
}

# Feste Adresse: API_EXTERNAL_URL und der DNS-Record sollen ein Stop/Start der
# VM überleben.
resource "google_compute_address" "vm" {
  name       = "${var.name_prefix}-ip"
  region     = var.region
  depends_on = [google_project_service.required]
}
