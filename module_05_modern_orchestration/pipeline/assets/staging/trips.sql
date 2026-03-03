/* @bruin
name: staging.trips
type: duckdb.sql
materialization:
  type: table
depends:
  - ingestion.trips
  - ingestion.payment_lookup
@bruin */

-- We are using 'trips' and 'payment_lookup' as the table names
-- Bruin's DuckDB connection usually puts these in the default search path
SELECT
    t.tpep_pickup_datetime as pickup_datetime,
    t.tpep_dropoff_datetime as dropoff_datetime,
    t.pu_location_id as pickup_location_id,
    t.do_location_id as dropoff_location_id,
    t.fare_amount,
    t.taxi_type,
    p.payment_type_name
FROM ingestion.trips t
LEFT JOIN ingestion.payment_lookup p
  ON t.payment_type = p.payment_type_id
