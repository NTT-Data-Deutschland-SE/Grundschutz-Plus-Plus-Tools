output "external_ip" {
  description = "Feste öffentliche Adresse der VM — Ziel des A-Records, falls DNS extern gepflegt wird."
  value       = google_compute_address.vm.address
}

output "ssh" {
  description = "SSH ohne offenen Port 22."
  value       = "gcloud compute ssh ${google_compute_instance.supabase.name} --zone ${var.zone} --project ${var.project_id} --tunnel-through-iap"
}

output "tunnel_api" {
  description = "Kong/PostgREST auf den eigenen Rechner holen — der Weg für die curl-Abnahme aus Phase 1."
  value       = "gcloud compute start-iap-tunnel ${google_compute_instance.supabase.name} 8000 --local-host-port=localhost:8000 --zone ${var.zone} --project ${var.project_id}"
}

output "tunnel_postgres" {
  description = "psql für die Migrationen aus Phase 1."
  value       = "gcloud compute start-iap-tunnel ${google_compute_instance.supabase.name} 5432 --local-host-port=localhost:5433 --zone ${var.zone} --project ${var.project_id}"
}

output "upload_app" {
  description = "Die neun Werkzeuge auf den statischen Host schieben (nur mit gesetztem domain sinnvoll)."
  value       = "gcloud compute scp --recurse --tunnel-through-iap --zone ${var.zone} --project ${var.project_id} ../../GS++-oscal-app/. ${google_compute_instance.supabase.name}:/opt/gpp/app/"
}

output "secret_commands" {
  description = "Die erzeugten Zugangsdaten auslesen. ANON_KEY und SERVICE_ROLE_KEY stehen in /opt/gpp/supabase/.env auf der VM."
  value = {
    for k, v in google_secret_manager_secret.this :
    k => "gcloud secrets versions access latest --secret=${v.secret_id} --project=${var.project_id}"
  }
}

output "app_url" {
  description = "Ursprung, unter dem Werkzeuge und API gemeinsam liegen."
  value       = local.tls_enabled ? "https://${var.domain}" : "(kein domain gesetzt — nur über den IAP-Tunnel auf http://localhost:8000)"
}
