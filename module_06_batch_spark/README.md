# Module 06: Distributed Batch Processing with Apache Spark

## 🏛️ Master Technical Report
This project represents a comprehensive implementation of high-volume computational analytics using the **Apache Spark 3.5.0** framework. The project transitions from single-node logic to a distributed parallel computation model, focusing on architectural integrity and storage optimization.

### 1. Architectural Synthesis
* **Infrastructure:** Orchestrated within a **WSL2 (Linux)** subsystem, utilizing Python 3.10 virtual environments.
* **Observability:** Established a networking bridge for the **Spark UI (Port 4040)**, enabling deep-packet inspection of the **DAG (Directed Acyclic Graph)** and task execution stages.
* **DevOps Integrity:** Refactored the repository into a standardized modular hierarchy with hardened `.gitignore` wildcards to ensure repository "thinness."

---

## 🛠️ Project Specifications & Tech Stack
* **Engine:** Apache Spark 3.5.0 (PySpark)
* **Storage Format:** **Apache Parquet** (Columnar Storage)
* **Runtime:** WSL2 / Ubuntu 22.04
* **Optimization:** **Predicate Pushdown** and **Column Pruning**

### 📐 Data Engineering & Schema Enforcement
To maintain data integrity, strict Spark DDL was applied to the **November 2025 Yellow Taxi** dataset. This prevents type-drift and ensures consistent analytical output across the distributed cluster.

### 📦 Storage Optimization Strategy
The raw dataset was repartitioned and converted into Parquet format:
* **Partition Size:** Optimized at **~25MB** per chunk.
* **Core Distribution:** Balanced across 4 partitions to maximize local CPU utilization and minimize I/O latency.

---

## 📊 Analytical Methodology & Insights
Using Spark SQL and DataFrame APIs, the following computational audits were performed:

| Metric | Result / Insight |
| :--- | :--- |
| **Peak Demand Day** | **November 15th** (Total trips: **162,604**) |
| **Temporal Anomaly** | Identified a max trip duration of **90.65 hours**. |
| **Zone Popularity** | **Governor's Island** yielded the minimum pickup frequency (n=1). |
| **Relational Algebra** | Executed a **Shuffle-Join** to enrich Fact data with Zone Dimensions. |

---

## 🚀 Local Execution & Reproducibility
To reproduce this pipeline in a local environment:

1. **Initialize Environment:**
   ```bash
   python -m venv env310
   source env310/bin/activate
   pip install -r pyproject.toml