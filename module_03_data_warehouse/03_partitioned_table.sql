-- Create a table partitioned by dropoff_datetime and clustered by VendorID
CREATE OR REPLACE TABLE `trips_data_all.yellow_tripdata_2024_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `trips_data_all.external_yellow_tripdata_2024`;