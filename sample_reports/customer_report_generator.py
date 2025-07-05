data = [(1, "Alice", "North"), (2, "Bob", "East"), (3, "Charlie", "West")]
columns = ["customer_id", "name", "region"]
df = spark.createDataFrame(data, columns)
df.write.mode("overwrite").saveAsTable("certified_customer_reports")
df.coalesce(1).write.mode("overwrite").csv("s3://output/reports/customers.csv", header=True)
