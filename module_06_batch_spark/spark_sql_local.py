import argparse
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# What: This function contains our Spark logic
# Why: To make the code modular and easy to run from the command line
def run_job(input_green, output):
    # Initialize the Spark Session
    # Note: We do NOT define .master() here because we will provide it via spark-submit
    spark = SparkSession.builder \
        .appName('test_local_standalone') \
        .getOrCreate()

    # Reading the local Parquet data we prepared earlier in Module 6
    print(f"Reading data from: {input_green}")
    df_green = spark.read.parquet(input_green)

    # Simple transformation: Select specific columns to create a smaller report
    # This proves the cluster is actually 'processing' the data
    df_result = df_green \
        .select('VendorID', 'lpep_pickup_datetime', 'PULocationID', 'DOLocationID') \
        .filter(df_green.VendorID == 2)

    # Writing the results back to your local folder
    print(f"Writing results to: {output}")
    df_result.write.mode("overwrite").parquet(output)

if __name__ == "__main__":
    # Using argparse to allow passing folder paths from the terminal
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_green', required=True)
    parser.add_argument('--output', required=True)
    
    args = parser.parse_args()

    run_job(input_green=args.input_green, output=args.output)