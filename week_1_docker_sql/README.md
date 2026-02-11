# 🚕 NYC Taxi Data Engineering Project (Week 1)

This repository documents the complete end-to-end setup of a data ingestion pipeline, moving from a local Python script to a fully orchestrated Docker environment.

---

## 🛠 The Tools We Used
* **Python (Pandas/SQLAlchemy):** To process and upload data in chunks.
* **Postgres:** Our relational database for storing taxi trips.
* **pgAdmin:** A web-based UI to look at our data.
* **Docker:** To package our code so it runs anywhere.
* **Docker Compose:** To run the Database and pgAdmin together automatically.

---

## 🏗 The 4 Stages of Development
1.  **Prototyping:** We used **Jupyter Notebooks** to test the data connection and clean the column names.
2.  **Automation:** we converted the notebook into `ingest_data.py` and added arguments so it can handle any month of data.
3.  **Containerization:** We built a **Dockerfile** so our script doesn't depend on our local computer's settings.
4.  **Orchestration:** We used **Docker Compose** to manage networking and persistent data volumes.

---
