from pyspark.sql.functions import col

df = spark.table("processed_sales_reports")
certified_df = df.filter((col("total_amount") > 0) & (col("region").isNotNull()))

certified_df.write.mode("overwrite").saveAsTable("certified_sales_reports")
