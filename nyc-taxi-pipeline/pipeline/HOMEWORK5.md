# Data Engineering Zoomcamp 2026 - Homework 5 Answers
**Project:** NYC Taxi Bruin Pipeline

## Question 1: Bruin Pipeline Structure
**Answer:** `.bruin.yml` and `pipeline/` with `pipeline.yml` and `assets/`  
*Note: In our current setup, the `.bruin.yml` defines the root, and we organized our logic inside the pipeline folder.*

## Question 2: Materialization Strategies
**Answer:** `time_interval` - incremental based on a time column  
*Note: This is the strategy we used with `--start-date` and `--end-date` to process specific months.*

## Question 3: Pipeline Variables
**Answer:** `bruin run --var 'taxi_types=["yellow"]'`  
*Note: Bruin expects variables passed via the `--var` flag using JSON-style formatting for arrays.*

## Question 4: Running with Dependencies
**Answer:** `bruin run --select ingestion.trips+`  
*Note: The `+` suffix tells Bruin to include the selected asset and all its downstream dependents.*

## Question 5: Quality Checks
**Answer:** `name: not_null`  
*Note: This is the standard Bruin check to ensure columns like `pickup_datetime` are never empty.*

## Question 6: Lineage and Dependencies
**Answer:** `bruin lineage`  
*Note: This command generates the visual or text-based representation of how your assets connect.*

## Question 7: First-Time Run
**Answer:** `--full-refresh`  
*Note: This flag forces Bruin to drop existing tables and recreate them, which is essential for the first run or schema changes.*