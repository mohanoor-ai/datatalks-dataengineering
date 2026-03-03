# 05_run_ui_fixed.py
from pyspark.sql import SparkSession
import time

# Initialize Spark with a specific BIND ADDRESS for WSL2
# We set 'spark.driver.bindAddress' to 127.0.0.1 to help the WSL bridge
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('zoomcamp_ui_fixed') \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.driver.host", "127.0.0.1") \
    .getOrCreate()

# Load data so the UI has "Jobs" to display
df = spark.read.parquet('../data/pq/yellow/2025/11/')
df.limit(10).show()

print("\n🚀 FIXED Spark UI should be available.")
print("👉 Try: http://localhost:4040")
print("👉 If that fails, try: http://127.0.0.1:4040")
print("⚠️ Keep this terminal open! Press CTRL+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    spark.stop()