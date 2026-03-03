# Terraform configuration for BigQuery Dataset
resource "google_bigquery_dataset" "dataset" {
  dataset_id = "trips_data_all"
  project    = "your-gcp-project-id"
  location   = "US"
}