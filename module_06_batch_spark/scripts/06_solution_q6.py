# 06_solution_q6.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize the Official 2026 Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('homework_q6_join') \
    .getOrCreate()

# 1. Load the Partitioned Taxi Data (November 2025)
df_taxi = spark.read.parquet('../data/pq/yellow/2025/11/')

# 2. Load the Zone Lookup Data
# Make sure you have downloaded this to data/raw/
df_zones = spark.read \
    .option("header", "true") \
    .csv('../data/raw/taxi_zone_lookup.csv')

# 3. Perform the JOIN
# We match PULocationID from the taxi data to LocationID in the zones data
df_joined = df_taxi.join(df_zones, df_taxi.PULocationID == df_zones.LocationID)

# 4. Group by 'Zone' and count occurrences
# Then sort by 'count' in ascending order to find the minimum
least_frequent = df_joined \
    .groupBy("Zone") \
    .count() \
    .orderBy("count", ascending=True)

# 5. Show the top result
print("--- THE LEAST FREQUENT PICKUP ZONE ---")
least_frequent.show(1)

spark.stop()
