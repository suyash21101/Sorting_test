# Databricks notebook source
# MAGIC %run "./Lib"
# MAGIC import Lib

# COMMAND ----------

arr = [3, 2, 1]
bubbleSort(arr)

# COMMAND ----------

# Import PySpark
import pyspark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

# COMMAND ----------


df = spark.table("hive_metastore.default.sorting_ds_1_csv")

l1 = df.select('Sort').rdd.flatMap(lambda x: x).collect()
Lib.bubbleSort(l1) 

