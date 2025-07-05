from pyspark.sql import Row

reports = [
    Row(report_id=1, name="Sales Report", owner="Finance", path="s3://output/reports/sales.csv", tags=["monthly", "finance"]),
    Row(report_id=2, name="Customer Report", owner="Sales", path="s3://output/reports/customers.csv", tags=["weekly", "crm"]),
]

spark.createDataFrame(reports).write.mode("overwrite").saveAsTable("report_catalog")
