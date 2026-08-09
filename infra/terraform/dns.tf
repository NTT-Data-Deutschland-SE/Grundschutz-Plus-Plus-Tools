resource "google_dns_record_set" "app" {
  count = var.dns_managed_zone != "" && local.tls_enabled ? 1 : 0

  name         = "${var.domain}."
  managed_zone = var.dns_managed_zone
  type         = "A"
  ttl          = 300
  rrdatas      = [google_compute_address.vm.address]
}

resource "google_billing_budget" "this" {
  count = var.billing_account != "" ? 1 : 0

  billing_account = var.billing_account
  display_name    = "${var.name_prefix}-supabase-test"

  budget_filter {
    projects = ["projects/${data.google_project.this.number}"]
  }

  amount {
    specified_amount {
      units = tostring(var.budget_amount)
    }
  }

  # 50 / 90 / 100 Prozent an die Rechnungsempfänger des Kontos.
  dynamic "threshold_rules" {
    for_each = [0.5, 0.9, 1.0]
    content {
      threshold_percent = threshold_rules.value
    }
  }

  depends_on = [google_project_service.required]
}

data "google_project" "this" {
  project_id = var.project_id
}
