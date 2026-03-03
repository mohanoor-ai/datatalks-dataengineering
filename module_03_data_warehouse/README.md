# Module 3: Data Warehouse (BigQuery)

This module covers the architecture and optimization of **Google BigQuery** for large-scale data analytics, specifically focusing on the 2024 Yellow Taxi dataset.

## 📚 Concepts Covered
* **External vs. Materialized Tables:** Querying GCS directly (cost-effective storage) vs. internal BQ storage (high-performance compute).
* **Columnar Storage:** Understanding how BigQuery processes specific columns to minimize data scan.
* **Partitioning:** Segmenting data by `tpep_dropoff_datetime` to prune unnecessary data.
* **Clustering:** Sorting data by `VendorID` within partitions for faster filtering.

## 🛠️ SQL Scripts & Infrastructure
* `01_external_table.sql`: Defining the schema-on-read link to GCS.
* `02_regular_table.sql`: Standard materialized table for performance benchmarking.
* `03_partitioned_table.sql`: Implementation of optimized partitioning and clustering.
* `04_bigquery_ml.sql`: Machine Learning (Linear Regression) directly in SQL.
* `main.tf`: Terraform configuration for BigQuery dataset provisioning.

---

## 🏆 BigQuery Best Practices
To maximize performance and minimize costs in the 2026 Zoomcamp:

1. **Avoid `SELECT *`:** Only query the columns you need. BigQuery is columnar; every extra column costs money.
2. **Filter by Partition:** Always include the partition column (e.g., `tpep_dropoff_datetime`) in your `WHERE` clause.
3. **Clustering Strategy:** Cluster by columns used frequently in filters or aggregations (e.g., `VendorID`).
4. **Denormalize Data:** Unlike traditional SQL, BigQuery handles wide, flat tables better than complex nested joins.
5. **Preview Data for Free:** Use the "Preview" tab in the UI to see data without running a query and incurring costs.

---