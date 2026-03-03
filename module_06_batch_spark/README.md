# Module 6: Batch Processing with Apache Spark

This module focuses on distributed data processing using **Apache Spark**. The goal was to move beyond single-node scripts and learn how to handle large datasets by leveraging Spark's parallel execution engine.

## Learning Objectives
* **Distributed Computing:** Understanding how Spark manages tasks across a cluster.
* **Storage Optimization:** Converting raw data into **Parquet** format for better compression and faster I/O.
* **Data Partitioning:** Repartitioning datasets to optimize CPU usage and parallel processing.
* **Transformations & Actions:** Using the Spark DataFrame API for filtering, grouping, and complex aggregations.
* **Relational Joins:** Joining large-scale fact tables (Taxi trips) with dimension tables (Zones) to enrich data.

## Technologies Used
* **Apache Spark 3.5.0**
* **PySpark**
* **Parquet**
* **WSL2 (Ubuntu)**

## Key Concepts Applied
* **Repartitioning:** Optimized the data layout by creating balanced 25MB partitions.
* **Spark SQL:** Used SQL syntax and temporary views for analytical queries.
* **Broadcast vs. Shuffle Joins:** Understanding how Spark moves data across the network during join operations.
* **Spark UI:** Monitored job stages and DAGs (Directed Acyclic Graphs) to troubleshoot performance.

---
*Back to the [Main Repository](../README.md)*