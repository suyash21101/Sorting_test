# Databricks notebook source
# MAGIC %run "./Lib"

# COMMAND ----------

arr = [3, 2, 1]
bubbleSort(arr)

# COMMAND ----------

df = spark.table("hive_metastore.default.sorting_ds_1_csv")

l1 = df.select('Sort').rdd.flatMap(lambda x: x).collect()
bubbleSort(l1) 

