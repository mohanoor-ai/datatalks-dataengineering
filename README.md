# Data Engineering Zoomcamp 2026 - Comprehensive Portfolio

**Author:** Mohammed Sheikh-Noor  
**Course:** DataTalks.Club Data Engineering Zoomcamp

---

## 📖 Project Overview
This repository contains the code, infrastructure, and orchestration pipelines developed during the **2026 Data Engineering Zoomcamp**. The overarching goal of these projects is to build a robust, scalable, and automated End-to-End Data Pipeline using the **NYC Taxi Dataset** (Yellow and Green trips).

Throughout this repository, raw data is extracted, loaded into data lakes/warehouses, transformed into analytical models, and rigorously tested for data quality.

---

## 🛠️ Modules Covered & Accomplishments

### 🔹 Module 1: Containerization & Infrastructure as Code (IaC)
* **The Goal:** To set up an isolated, reproducible local environment and provision cloud resources programmatically.
* **Technologies:** Docker, PostgreSQL, pgAdmin, Terraform, GCP.
* **Key Accomplishments:**
    * Containerized a local PostgreSQL and pgAdmin environment.
    * Developed a Python ingestion script with chunking logic to handle large-scale CSV loads into Postgres.
    * Utilized **Terraform** to automate the provisioning of GCS buckets and BigQuery datasets.

### 🔹 Module 2: Workflow Orchestration
* **The Goal:** To automate the data pipeline via scheduled triggers and dependency management.
* **Technologies:** Kestra, Google Cloud Storage (GCS), BigQuery.
* **Key Accomplishments:**
    * Designed Directed Acyclic Graphs (DAGs) using YAML to orchestrate web-to-GCS data flows.
    * Implemented backfilling logic for historical taxi data loads.

### 🔹 Module 3: Cloud Data Warehousing
* **The Goal:** To optimize storage for high-performance, cost-effective analytical querying.
* **Technologies:** Google BigQuery, SQL.
* **Key Accomplishments:**
    * Implemented **Partitioning** (by pickup datetime) and **Clustering** (by VendorID) to optimize query performance and reduce cloud costs.
    * Evaluated performance deltas between External and Materialized tables.

### 🔹 Module 4: Analytics Engineering
* **The Goal:** To transform raw data into business-ready data models (The "T" in ELT).
* **Technologies:** dbt (Data Build Tool), BigQuery, SQL.
* **Key Accomplishments:**
    * Built a modular architecture separating data into **Staging** and **Core** layers.
    * Unified Yellow and Green taxi data into a single `fact_trips` table with integrated data quality testing.

### 🔹 Module 5: Modern Pipeline Orchestration & Micro-Pipelines
* **The Goal:** To build lightweight, code-first pipelines with built-in quality checks.
* **Technologies:** Bruin, DuckDB, dlt (Data Load Tool).
* **Key Accomplishments:**
    * Architected a local analytical pipeline using **DuckDB** and **Bruin**.
    * Resolved file-locking concurrency challenges through explicit pipeline dependency mapping.

### 🔹 Module 6: Batch Processing with Apache Spark
* **The Goal:** To execute distributed parallel computation on large-scale datasets.
* **Technologies:** Apache Spark 3.5.0, PySpark, Parquet.
* **Key Accomplishments:**
    * Configured a Spark cluster on **WSL2** and established a port-forwarding bridge for the **Spark UI**.
    * Optimized data storage by repartitioning datasets into **25MB Parquet** files.
    * Performed heavy-duty transformations including **Shuffle-Joins** and complex aggregations on millions of records.

---

## 📂 Repository Structure
```text
.
├── module_01_docker_sql/          # Infrastructure & Containerization
├── module_02_orchestration/      # Pipeline Automation (Kestra)
├── module_03_data_warehouse/     # BigQuery & Partitioning logic
├── module_04_analytics_engineering/ # dbt Transformation models
├── module_06_batch_spark/        # Distributed Batch Processing (Spark)
└── README.md                     # Master Documentation