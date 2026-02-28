# Module 5: Data Orchestration with Bruin (NYC Taxi)

This project implements a data pipeline to ingest, stage, and report on NYC Yellow Taxi trip data using **Bruin** and **DuckDB**.

## 🚀 Project Overview
The goal of this pipeline is to automate the flow of taxi data from cloud storage into a local analytical database, ensuring data quality at every step.

### 🏗️ Architecture & Folder Structure
The project is organized to separate the orchestration logic from the data assets:

- `pipeline/`: Contains the master `pipeline.yml` orchestration file.
- `assets/`: 
    - `ingestion/`: Python scripts (`trips.py`, `payment_lookup.py`) using `dlt` for data movement.
    - `staging/`: SQL models for cleaning and transforming raw data.
    - `reports/`: Final analytical views for reporting.

## 🛠️ Tech Stack
- **Orchestrator:** Bruin
- **Database:** DuckDB (Local)
- **Ingestion Engine:** dlt (Data Load Tool)
- **Language:** Python & SQL

## ⚙️ How to Run
To run the pipeline for a specific month (e.g., January 2022), use the following command from the project root:

```powershell
bruin run pipeline/pipeline.yml --start-date 2022-01-01 --end-date 2022-02-01 --workers 1