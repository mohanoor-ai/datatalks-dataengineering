# 03_solution_q3.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('homework_q3') \
    .getOrCreate()

# Read the partitioned data we just created
df = spark.read.parquet('../data/pq/yellow/2025/11/')

# Filter for November 15th, 2025
# We use F.to_date to ensure we are only looking at the calendar day
trips_on_15th = df \
    .filter(F.to_date(df.tpep_pickup_datetime) == '2025-11-15') \
    .count()

print(f"✅ Number of taxi trips on November 15th: {trips_on_15th}")
spark.stop()