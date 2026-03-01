# Workshop 1: Ingestion with dlt for Data Engineering Zoomcamp 2026

In this workshop, I implemented a data ingestion pipeline using **dlt** (Data Load Tool) integrated within the **Bruin** orchestrator. The data was loaded into a **DuckDB** instance for analysis.

---

### Question 1. What is the start date and end date of the dataset? (1 point)

* 2009-01-01 to 2009-01-31
* 2009-06-01 to 2009-07-01
* **2024-01-01 to 2024-02-01**
* 2024-06-01 to 2024-07-01

> **Verification SQL:**
> ```sql
> SELECT min(tpep_pickup_datetime), max(tpep_pickup_datetime) FROM ingestion.trips;
> ```

---

### Question 2. What proportion of trips are paid with credit card? (1 point)

* 16.66%
* 26.66%
* **36.66%**
* 46.66%

> **Verification SQL:**
> ```sql
> SELECT (count(CASE WHEN payment_type = 1 THEN 1 END) * 100.0 / count(*)) as cc_percentage 
> FROM ingestion.trips;
> ```

---

### Question 3. What is the total amount of money generated in tips? (1 point)

* $4,063.41
* **$6,063.41**
* $8,063.41
* $10,063.41

> **Verification SQL:**
> ```sql
> SELECT sum(tip_amount) FROM ingestion.trips;
> ```

---

### Pipeline Environment
* **Destination:** DuckDB
* **Orchestration:** Bruin CLI
* **Ingestion:** dlt (Data Load Tool)