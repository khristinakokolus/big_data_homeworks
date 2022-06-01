from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName('CountRows').getOrCreate()
    df = spark.read.csv('PS_20174392719_1491204439457_log.csv')
    all_rows_count = df.count()

    print("Total number of rows in the dataset: ", all_rows_count)


if __name__ == '__main__':
    main()

