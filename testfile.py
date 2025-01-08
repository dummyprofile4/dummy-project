# Databricks notebook source
dbutils.fs.ls('/')

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/power-plant/data/')

# COMMAND ----------

df = spark.read.csv('dbfs:/databricks-datasets/power-plant/data/Sheet1.tsv')

# COMMAND ----------

df.limit(5).show()
