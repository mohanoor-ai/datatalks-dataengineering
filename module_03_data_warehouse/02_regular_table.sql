-- Create a regular (materialized) table from the external table
CREATE OR REPLACE TABLE `trips_data_all.yellow_tripdata_2024` AS
SELECT * FROM `trips_data_all.external_yellow_tripdata_2024`;