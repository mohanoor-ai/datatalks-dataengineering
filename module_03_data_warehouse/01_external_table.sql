-- Create an external table pointing to the 2024 Yellow Taxi Parquet files
CREATE OR REPLACE EXTERNAL TABLE `trips_data_all.external_yellow_tripdata_2024`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://your-bucket-name/yellow_tripdata_2024-*.parquet']
);