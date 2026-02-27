/** @bruin
name: raw.taxi_zone_lookup
type: duckdb.sql
materialization:
   type: table
@bruin */
SELECT * FROM read_csv_auto('https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv');
