# What: Spark SQL script for GCS Standalone execution
# Why: To process data stored in Google Cloud using our local cluster
import argparse
import pyspark
from pyspark.sql import SparkSession

def run_job(input_green, output):
    # We initialize the session with specific GCS configurations
    spark = SparkSession.builder \
        .appName('test_gcs_standalone') \
        .getOrCreate()

    # Configuring Spark to use the GCS Connector logic
    hadoop_conf = spark._jsc.hadoopConfiguration()
    
    # These two settings tell Spark WHERE to find your 'Passport'
    hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
    hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
    hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", "/home/moha_/.google/credentials/google_credentials.json")
    hadoop_conf.set("fs.gs.auth.service.account.enable", "true")

    print(f"Reading data from GCS: {input_green}")
    df_green = spark.read.parquet(input_green)

    # Simple transformation
    df_result = df_green \
        .select('VendorID', 'lpep_pickup_datetime', 'PULocationID', 'DOLocationID')

    print(f"Writing results back to GCS: {output}")
    df_result.write.mode("overwrite").parquet(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_green', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    run_job(input_green=args.input_green, output=args.output)