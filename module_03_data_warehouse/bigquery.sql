-- Querying External Table
SELECT count(*) FROM `trips_data_all.external_yellow_tripdata`;

-- Create a non-partitioned table from external table
CREATE OR REPLACE TABLE `trips_data_all.yellow_tripdata_non_partitioned` AS
SELECT * FROM `trips_data_all.external_yellow_tripdata`;

-- Create a partitioned table
CREATE OR REPLACE TABLE `trips_data_all.yellow_tripdata_partitioned`
PARTITION BY DATE(tpep_pickup_datetime) AS
SELECT * FROM `trips_data_all.external_yellow_tripdata`;

-- Impact of Partitioning
SELECT DISTINCT(VendorID)
FROM `trips_data_all.yellow_tripdata_non_partitioned`
WHERE DATE(tpep_pickup_datetime) BETWEEN '2024-01-01' AND '2024-06-30';

SELECT DISTINCT(VendorID)
FROM `trips_data_all.yellow_tripdata_partitioned`
WHERE DATE(tpep_pickup_datetime) BETWEEN '2024-01-01' AND '2024-06-30';