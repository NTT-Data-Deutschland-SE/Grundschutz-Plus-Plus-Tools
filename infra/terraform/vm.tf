resource "google_compute_instance" "supabase" {
  name         = "${var.name_prefix}-supabase"
  machine_type = var.machine_type
  zone         = var.zone
  tags         = [local.tag]

  # Beim Zerstören soll nichts an einem laufenden Prozess scheitern.
  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
      size  = var.boot_disk_gb
      type  = "pd-balanced"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.subnet.id

    access_config {
      nat_ip = google_compute_address.vm.address
    }
  }

  shielded_instance_config {
    enable_secure_boot          = true
    enable_vtpm                 = true
    enable_integrity_monitoring = true
  }

  service_account {
    email  = google_service_account.vm.email
    scopes = ["cloud-platform"]
  }

  metadata = {
    enable-oslogin = "TRUE"

    gpp-domain       = var.domain
    gpp-supabase-ref = var.supabase_ref
    gpp-admin-email  = var.admin_email
    gpp-secret-pg    = google_secret_manager_secret.this["postgres-password"].secret_id
    gpp-secret-jwt   = google_secret_manager_secret.this["jwt-secret"].secret_id
    gpp-secret-dash  = google_secret_manager_secret.this["dashboard-password"].secret_id
    gpp-secret-admin = google_secret_manager_secret.this["admin-password"].secret_id
  }

  metadata_startup_script = file("${path.module}/startup.sh")

  depends_on = [
    google_secret_manager_secret_version.this,
    google_secret_manager_secret_iam_member.vm,
    terraform_data.guard_allowed_cidrs,
  ]

  lifecycle {
    # Ein geändertes Startskript soll die VM nicht ersetzen — es läuft bei
    # jedem Boot erneut und ist idempotent geschrieben.
    ignore_changes = [metadata_startup_script]
  }
}
