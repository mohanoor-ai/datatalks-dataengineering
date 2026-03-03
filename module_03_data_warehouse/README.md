# Module 3: Data Warehouse (BigQuery)

This module covers the fundamentals of Data Warehousing using Google BigQuery, focusing on the 2024 Yellow Taxi dataset.

## 📚 Concepts Covered
* **External vs. Materialized Tables:** Understanding when to query GCS directly vs. storing data in BQ.
* **Columnar Storage:** Why querying specific columns (PULocationID) is cheaper than `SELECT *`.
* **Partitioning:** Reducing data scan by segmenting tables by `tpep_dropoff_datetime`.
* **Clustering:** Improving filter/sort performance by grouping data by `VendorID`.

## 🛠️ SQL Scripts
* `01_external_table.sql`: Defines the connection to GCS Parquet files.
* `02_regular_table.sql`: Creates a standard BQ table for performance benchmarking.
* `03_partitioned_table.sql`: Implements the optimized storage strategy.

# BigQuery Best Practices (Module 3)

* **Filter by Partition:** Always use the partition column (`tpep_dropoff_datetime`) in the `WHERE` clause.
* **Denormalize:** BigQuery performs best with flat, denormalized tables rather than deep joins.
* **Avoid `SELECT *`:** Only query the columns you need to save on processing costs.
* **Clustering Order:** Order columns in `CLUSTER BY` from lowest to highest cardinality.