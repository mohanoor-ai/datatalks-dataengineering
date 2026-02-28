# 🚀 Data Engineering Zoomcamp 2026 - Comprehensive Portfolio

**Author:** Mohammed Sheikh-Noor
**Course:** [DataTalks.Club Data Engineering Zoomcamp](https://datatalks.club/)

## 📖 Project Overview
This repository contains the code, infrastructure, and orchestration pipelines developed during the 2026 Data Engineering Zoomcamp. The overarching goal of these projects is to build a robust, scalable, and automated End-to-End Data Pipeline using the **NYC Taxi Dataset** (Yellow and Green trips). 

Throughout this repository, raw data is extracted, loaded into data lakes/warehouses, transformed into analytical models, and rigorously tested for data quality.

---

## 🛠️ Modules Covered & Accomplishments

### 🔹 Module 1: Containerization & Infrastructure as Code (IaC)
**The Goal:** To set up an isolated, reproducible local environment and provision cloud resources programmatically.
- **Technologies Used:** Docker, Docker-Compose, PostgreSQL, pgAdmin, Terraform, Google Cloud Platform (GCP).
- **Key Accomplishments:**
  - Containerized a local PostgreSQL database and pgAdmin for local data exploration.
  - Wrote a Python ingestion script (`ingest_data.py`) to chunk and load large CSV files into Postgres to avoid memory crashes.
  - Utilized **Terraform** to provision GCP resources (Google Cloud Storage buckets and BigQuery datasets) automatically, ensuring infrastructure is treated as version-controlled code.

### 🔹 Module 2: Workflow Orchestration
**The Goal:** To automate the data pipeline so it runs on a schedule without manual intervention.
- **Technologies Used:** Kestra / Mage, Google Cloud Storage (GCS), BigQuery.
- **Key Accomplishments:**
  - Designed Directed Acyclic Graphs (DAGs) using YAML/Python configurations to orchestrate the flow of data.
  - Extracted taxi data from public web sources, temporarily staged it, and loaded it into Google Cloud Storage.
  - Created scheduled triggers and handled backfilling for historical data loads.

### 🔹 Module 3: Cloud Data Warehousing
**The Goal:** To optimize data storage for fast, cost-effective analytical querying.
- **Technologies Used:** Google BigQuery, SQL.
- **Key Accomplishments:**
  - Created external tables in BigQuery pointing directly to parquet files in GCS.
  - Implemented **Partitioning** (by `pickup_datetime`) and **Clustering** (by `VendorID`) to drastically reduce the amount of data scanned during queries, saving both time and cloud computing costs.
  - Evaluated the performance differences between materialized and external tables.

### 🔹 Module 4: Analytics Engineering
**The Goal:** To transform raw data into structured, business-ready data models (The "T" in ELT).
- **Technologies Used:** dbt (Data Build Tool), BigQuery, SQL.
- **Key Accomplishments:**
  - Built a modular data architecture separating data into **Staging** (cleaning and standardizing types) and **Core** (business logic).
  - Created a unified `fact_trips` table by joining Yellow and Green taxi data with a `dim_zones` lookup table.
  - Integrated testing directly into the models (e.g., checking for unique trip IDs and non-null values) and generated automated documentation and lineage graphs.

### 🔹 Module 5: Modern Pipeline Orchestration (Current)
**The Goal:** To build a lightweight, code-first data pipeline with built-in data quality checks.
- **Technologies Used:** Bruin, DuckDB, Python (dlt library).
- **Key Accomplishments:**
  - Designed a local, lightning-fast analytical pipeline using **DuckDB**.
  - Orchestrated Python ingestion scripts (using `dlt` for memory-safe chunking) and SQL staging models via **Bruin**.
  - Resolved concurrency challenges (DuckDB file locks) by explicitly defining pipeline dependencies (`depends:`).
  - Enforced strict data quality using Bruin's native checks (`not_null`, `unique`) directly within the pipeline YAML.

---

## 📁 Repository Structure
```text
.
├── nyc-taxi-pipeline/      # Module 5: Bruin orchestrator, DuckDB assets, and Homework
├── module_2_orchestration/ # Module 2: Workflow DAGs and configurations
├── week_1_docker_sql/      # Module 1: Dockerfiles, Postgres setup, and Python scripts
└── README.md               # Master Documentation