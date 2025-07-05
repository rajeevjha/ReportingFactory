df = spark.table("certified_sales_reports")
df.coalesce(1).write.mode("overwrite").csv("s3://output/reports/sales.csv", header=True)
