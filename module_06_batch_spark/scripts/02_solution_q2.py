# 02_solution_q2.py
import os
from pyspark.sql import SparkSession

# 1. Initialize the Official 2026 Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('homework_q2') \
    .getOrCreate()

# 2. Read the 2025-11 Parquet file we downloaded to data/raw/
input_path = '../data/raw/yellow_tripdata_2025-11.parquet'
df = spark.read.parquet(input_path)

# 3. OFFICIAL REQUIREMENT: Repartition to 4
# This forces Spark to redistribute the data into 4 equal chunks
df_repartitioned = df.repartition(4)

# 4. Save to the partitioned folder
output_path = '../data/pq/yellow/2025/11/'
df_repartitioned.write.mode("overwrite").parquet(output_path)

print("✅ Partitioning complete. Check the folder for file sizes.")
spark.stop()