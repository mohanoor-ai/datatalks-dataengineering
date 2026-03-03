# 04_solution_q4.py
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('homework_q4') \
    .getOrCreate()

# Read the partitioned data
df = spark.read.parquet('../data/pq/yellow/2025/11/')

# 1. Calculate duration in seconds
# 2. Convert seconds to hours (divide by 3600)
# 3. Find the maximum value
df_with_duration = df.withColumn(
    'trip_duration_hours',
    (F.unix_timestamp(df.tpep_dropoff_datetime) - F.unix_timestamp(df.tpep_pickup_datetime)) / 3600
)

longest_trip = df_with_duration.select(F.max('trip_duration_hours')).collect()[0][0]

print(f"✅ The longest trip in November 2025 was: {longest_trip:.2f} hours")
spark.stop()