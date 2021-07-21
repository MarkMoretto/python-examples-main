
"""
Purpose: Quick NLP
Date created: 2021-07-19

https://github.com/Apress/machine-learning-with-pyspark/blob/master/chapter_9_NLP/NLP_PySpark.ipynb

Contributor(s):
    Mark M.
"""

# --- Set Java version -- #
from os import environ

java8_path: str = r"C:\Java\jdk1.8.0_191"

environ["JAVA_HOME"] =  java8_path
environ["PATH"] = environ["JAVA_HOME"] + "/bin;" + environ["PATH"]



#######
from pyspark.sql import SparkSession

from pyspark.sql.functions import col, length, rand, udf
from pyspark.sql.types import IntegerType
from pyspark.ml.feature import (
        CountVectorizer,
        HashingTF,
        IDF,
        StopWordsRemover,
        Tokenizer,
        VectorAssembler,
        )

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder.appName("quickNLP").getOrCreate()

df=spark.createDataFrame([(1,'I really liked this movie'),
                         (2,'I would recommend this movie to my friends'),
                         (3,'movie was alright but acting was horrible'),
                         (4,'I am never watching that movie ever again')],
                        ['user_id','review'])


tknzr = Tokenizer(inputCol = "review", outputCol = "tokens")
df_tkn = tknzr.transform(df)


spark.stop()