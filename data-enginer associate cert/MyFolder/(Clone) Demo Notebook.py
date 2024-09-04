# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "hello world from sql!"

# COMMAND ----------

# MAGIC %md
# MAGIC # Title !
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC

# COMMAND ----------

# MAGIC %run /Demo/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets/")
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


