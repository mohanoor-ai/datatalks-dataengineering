import pyspark
from pyspark.sql import SparkSession

# This command tells Spark to use all CPUs on your Lenovo (*) 
# and names the app so you can find it in the Spark UI.
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('zoomcamp_test') \
    .getOrCreate()

print(f"✅ Handshake Successful! Spark Version: {spark.version}")

# Always stop the session to free up your RAM
spark.stop()