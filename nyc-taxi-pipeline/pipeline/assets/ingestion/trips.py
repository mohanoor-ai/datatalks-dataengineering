"""@bruin
name: ingestion.trips
connection: duckdb-default
materialization:
  type: table
@bruin"""
import pandas as pd

def materialize(variables=None):
    # Using a direct link to ensure data is found
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-01.parquet"
    print(f"Downloading data from {url}...")
    
    df = pd.read_parquet(url).head(5000)
    df['taxi_type'] = 'yellow'
    
    print(f"Returning DataFrame with {len(df)} rows to Bruin.")
    return df
