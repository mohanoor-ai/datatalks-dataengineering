# Data Engineering Zoomcamp 2026 - Comprehensive Portfolio

**Author:** Mohammed Sheikh-Noor  
**Course:** DataTalks.Club Data Engineering Zoomcamp

---

## 📖 Project Overview
This repository contains the code, infrastructure, and orchestration pipelines developed during the **2026 Data Engineering Zoomcamp**. The objective is to build a robust, scalable, and automated End-to-End Data Pipeline using the **NYC Taxi Dataset**.

---

## 🛠️ Modules Covered & Accomplishments

### 🔹 [Module 1: Containerization & Infrastructure as Code (IaC)](./module_01_docker_sql)
* **Goal:** Reproducible local environments and automated cloud provisioning.
* **Tech:** Docker, PostgreSQL, Terraform, GCP.
* **Key Accomplishments:** Containerized Postgres and provisioned GCS/BigQuery resources using HCL.

### 🔹 [Module 2: Workflow Orchestration](./module_02_orchestration)
* **Goal:** Pipeline automation and scheduling.
* **Tech:** Kestra, Google Cloud Storage, BigQuery.
* **Key Accomplishments:** Developed DAGs for automated web-to-GCS data transfers and historical backfills.

### 🔹 [Module 3: Cloud Data Warehousing](./module_03_data_warehouse)
* **Goal:** High-performance storage and cost optimization.
* **Tech:** Google BigQuery, SQL.
* **Key Accomplishments:** Implemented Partitioning and Clustering strategies to optimize query execution and minimize cloud costs.

### 🔹 [Module 4: Analytics Engineering](./module_04_analytics_engineering)
* **Goal:** Transforming raw data into business-ready models.
* **Tech:** dbt (Data Build Tool), BigQuery, SQL.
* **Key Accomplishments:** Developed modular staging and core layers, unifying datasets into a tested `fact_trips` model.

### 🔹 [Module 6: Batch Processing with Apache Spark](./module_06_batch_spark)
* **Goal:** Distributed parallel computation on large-scale datasets.
* **Tech:** Apache Spark 3.5.0, PySpark, Parquet.
* **Key Accomplishments:** Configured Spark on WSL2, optimized storage via 25MB Parquet partitions, and executed complex Shuffle-Joins.

---

## 📂 Repository Structure
```text
.
├── module_01_docker_sql/          # Containerization & IaC
├── module_02_orchestration/      # Workflow Automation
├── module_03_data_warehouse/     # Cloud Warehousing
├── module_04_analytics_engineering/ # Transformation (dbt)
├── module_06_batch_spark/        # Batch Processing (Spark)
└── README.md                     # Master Documentation