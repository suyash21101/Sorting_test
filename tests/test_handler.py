import tkinter as tk
from PIL import Image,ImageTk

window = tk.Tk()
window.title("SW Mini Project")
window.geometry("700x500")

def button_handler():
    twitter_handle_input = entry.get()
    text = tk.Text(master=window,height=1,width=10)
    text.grid(column=1,row=5)
    text.insert(tk.END,twitter_handle_input)

label1 = tk.Label(text ="Botometer and Sentiment Analysis", font=("Times new roman",20))
label1.grid(column=0,row=0, padx=20, pady=20)

label2 = tk.Label(text ="Enter the twitter handle: ", font=("Times new roman",15))
label2.grid(column=0,row=1, padx=10, pady=10)

button=tk.Button(window,text="Check (Bots/Sentiment)",command=button_handler,bg="red")
button.grid(column=0,row=2, padx=10, pady=10)

entry = tk.Entry()
entry.grid(column=1,row=1, padx=20, pady=20)

image=Image.open('twitter_image.jpg')
image.thumbnail((300,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label_image=tk.Label(image=photo)
label_image.grid(column=0,row=5)

window.mainloop()


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
print(arr)

# COMMAND ----------

# Import PySpark
#import pyspark
#from pyspark.sql import SparkSession

#Create SparkSession
#spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()

# COMMAND ----------


#df = spark.table("hive_metastore.default.sorting_ds_1_csv")

#l1 = df.select('Sort').rdd.flatMap(lambda x: x).collect()


