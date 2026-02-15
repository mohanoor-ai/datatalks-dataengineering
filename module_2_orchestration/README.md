# Module 2: Workflow Orchestration & AI Integration (2026 Zoomcamp)

This project documents my journey through Module 2 of the Data Engineering Zoomcamp. I transitioned from manual data scripts to a fully automated, cloud-native orchestration system using **Kestra**, **Google Cloud Platform (GCP)**, and **Generative AI**.

---

## 🏗️ The Architecture
The pipeline follows a modern **ELT (Extract, Load, Transform)** pattern:
1. **Extraction**: Automated `wget` tasks pull raw NYC Taxi data (Yellow and Green) from GitHub.
2. **Staging**: Data is compressed and moved to **Google Cloud Storage (GCS)** buckets for durable storage.
3. **Ingestion**: Raw data is loaded into **BigQuery** external tables.
4. **Production**: A `MERGE` statement moves data into partitioned production tables, ensuring **idempotency** (no duplicate rows if the flow runs twice).

---

## 🚀 Detailed Tutorial: What I Built

### 1. Robust Data Pipelines (Flows 08 & 09)
I engineered a system capable of handling millions of records across multiple years (2019-2021).
* **Smart Upserts**: Instead of simple appends, I used BigQuery `MERGE`. This allows the pipeline to update existing records or insert new ones based on the `unique_key`, making the pipeline "self-healing."
* **Handling History**: I utilized Kestra's **Backfill** engine. This allowed me to trigger historical runs for 3 years of taxi data in a single click, automatically iterating through monthly partitions.
* **Security First**: I implemented Kestra’s **KV Store** to inject GCP Service Account credentials dynamically, ensuring no sensitive JSON keys were hardcoded or committed to GitHub.

### 2. AI & RAG Integration (Flows 10 & 11)
I integrated **Google Gemini 1.5 Flash** directly into the orchestration layer to solve the "Hallucination Problem" in Data Engineering.
* **The Experiment**: I queried the AI about Kestra 1.1 features. 
* **The Failure (Non-RAG)**: The model confidently provided incorrect release dates (2022) and generic features based on outdated training data.
* **The Success (RAG)**: By building a **Retrieval-Augmented Generation** flow, I passed the real Nov 2025 release notes as context. The AI pivoted to 100% accuracy, proving that Data Engineers can ground LLMs in real-time "truth."

---

## 📂 Project Structure & Roadmap

| Section | Flows | Focus Area |
| :--- | :--- | :--- |
| **Foundations** | `01` - `05` | Variables, Inputs, and If-Else logic for flow control. |
| **Infra-as-Code** | `06` - `07` | Programmatically creating GCS buckets and BigQuery datasets. |
| **Big Data ELT** | `08` - `09` | Massive data movement, scheduling, and backfilling. |
| **AI Layer** | `10` - `11` | Gemini 1.5 integration and RAG context testing. |

---

## 🛠️ How to Run
### 1. Prerequisites
* **Kestra**: Running via Docker Compose.
* **GCP Setup**: A Service Account with `Storage Admin` and `BigQuery Admin` roles.
* **API Keys**: A Gemini API key from Google AI Studio.

### 2. Configuration
Add the following to your Kestra **KV Store** (Namespace: `zoomcamp`):
* `GCP_PROJECT_ID`: Your project ID.
* `GCP_CREDS`: Your Service Account JSON.
* `GEMINI_API_KEY`: Your Gemini API Key.

### 3. Deployment
1. Import the `.yaml` files into your Kestra instance.
2. Run `07_gcp_setup` first to prepare the cloud environment.
3. Use the **Backfill** button on `09_gcp_taxi_scheduled` to load historical data.