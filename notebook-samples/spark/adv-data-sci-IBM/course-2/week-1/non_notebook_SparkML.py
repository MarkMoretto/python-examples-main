

"""
Purpose: 
Date created: 2020-04-20

Contributor(s):
    Mark M.
"""

import os
data_folder = r"C:\Users\Work1\Desktop\School\coursera\IBM-Advanced-Data-Science\notebooks\adv-ml-and-sp"
folder = r"C:\Users\Work1\Desktop\School\coursera\IBM-Advanced-Data-Science\non-notebooks\adv-ml-and-sp"
os.chdir(folder)
import gc

from pyspark import SparkContext
from pyspark.sql import SparkSession

from pyspark.sql.types import StructType, StructField, IntegerType
from pyspark.ml.feature import StringIndexer
from pyspark.sql.functions import lit
gc.enable()

sc = SparkContext(appName="teethies")
spark = SparkSession.builder.getOrCreate()


schema_ = StructType([
        StructField("x", IntegerType(), True),
        StructField("y", IntegerType(), True),
        StructField("z", IntegerType(), True),
        ])

# Path to top-level folder in data set repo
data_folder_path = rf"{data_folder}\hmp-dataset"

# Empty dataframe variable as placeholder
df = None

for root, _, files in os.walk(data_folder_path):
    if "_" in root:

        foldername = os.path.basename(root)

        for f in files:
            filepath = rf"{root}\{f}"

            tmp_df = spark.read.option("header", "false").option("delimiter", " ").csv(filepath, schema=schema_)

            # Create a column called "source" storing the current CSV file
            tmp_df = tmp_df.withColumn("source", lit(f))
            
            # Create a column called "class" storing the current data folder
            tmp_df = tmp_df.withColumn("class", lit(foldername))
    
    
            if df is None:
                df = tmp_df
            else:
                df = df.union(tmp_df)
    gc.collect()



indxr = StringIndexer(inputCol="class", outputCol="classIndex")
indxd = indxr.fit(df).transform(df)

indxd.show()







spark.stop()
sc.stop()
