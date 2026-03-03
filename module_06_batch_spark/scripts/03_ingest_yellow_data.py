# 03_ingest_yellow_data.py
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import types

# 1. Official 2026 Spark Session Setup
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('official_zoomcamp_ingest') \
    .getOrCreate()

# 2. Official 2026 Yellow Taxi Schema
schema = types.StructType([
    types.StructField("VendorID", types.IntegerType(), True),
    types.StructField("tpep_pickup_datetime", types.TimestampType(), True),
    types.StructField("tpep_dropoff_datetime", types.TimestampType(), True),
    types.StructField("passenger_count", types.IntegerType(), True),
    types.StructField("trip_distance", types.DoubleType(), True),
    types.StructField("RatecodeID", types.IntegerType(), True),
    types.StructField("store_and_fwd_flag", types.StringType(), True),
    types.StructField("PULocationID", types.IntegerType(), True),
    types.StructField("DOLocationID", types.IntegerType(), True),
    types.StructField("payment_type", types.IntegerType(), True),
    types.StructField("fare_amount", types.DoubleType(), True),
    types.StructField("extra", types.DoubleType(), True),
    types.StructField("mta_tax", types.DoubleType(), True),
    types.StructField("tip_amount", types.DoubleType(), True),
    types.StructField("tolls_amount", types.DoubleType(), True),
    types.StructField("improvement_surcharge", types.DoubleType(), True),
    types.StructField("total_amount", types.DoubleType(), True),
    types.StructField("congestion_surcharge", types.DoubleType(), True)
])

# 3. Read the Official 2025-11 Dataset
# Path follows the standard: data/raw/yellow_tripdata_2025-11.csv
input_path = 'data/raw/yellow_tripdata_2025-11.csv'
df = spark.read \
    .option("header", "true") \
    .schema(schema) \
    .csv(input_path)

# 4. OFFICIAL REQUIREMENT: Repartition to 4
df = df.repartition(4)

# 5. Save to Parquet using Official Pathing
df.write.mode("overwrite").parquet('data/pq/yellow/2025/11/')

print("✅ Official 2025-11 Data Ingested and Partitioned to 4!")
spark.stop()