# Databricks notebook source
def bubbleSort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


# COMMAND ----------

arr = [3, 2, 1, 8, 10, 3, 19, 88, 92, 100, 86, 77, 28, 11]
bubbleSort(arr)

# COMMAND ----------

# Import PySpark
#import pyspark
#from pyspark.sql import SparkSession

#Create SparkSession
#spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

# COMMAND ----------


#df = spark.table("hive_metastore.default.sorting_ds_1_csv")

#l1 = df.select('Sort').rdd.flatMap(lambda x: x).collect()


