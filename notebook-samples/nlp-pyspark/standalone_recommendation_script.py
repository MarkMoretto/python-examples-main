
"""
Purpose: 
Date created: 2021-07-18

Contributor(s):
    Mark M.
"""

# from os import environ

# java8_path: str = r"C:\Java\jdk1.8.0_191"

# environ["JAVA_HOME"] =  java8_path
# environ["PATH"] = environ["JAVA_HOME"] + "/bin;" + environ["PATH"]


import re
import sys
from pathlib import Path
from operator import add
import urllib.request as ureq
from io import BytesIO, StringIO

# Third party libraries
import orjson
import lxml.etree
import pandas as pd

pd.set_option("display.max_columns", 10)
pd.set_option("display.max_colwidth", None)

xml_raw_url: str = "https://github.com/oxford-cs-deepnlp-2017/practical-1/blob/master/ted_en-20160408.xml?raw=true"

def get_xml_data(url):
    with ureq.urlopen(url) as resp:
        if resp.status == 200:
            _raw = BytesIO(resp.read())
            _xml_T = lxml.etree.parse(_raw)
    return _xml_T



def get_common_contractions():
    wiki_url = "https://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions"
    dfs = pd.read_html(wiki_url)
    _df = dfs[1]
    return _df["Contraction"].values.tolist()


# We will just remove any common contractions for simplicity
contractions = get_common_contractions()
assert (isinstance(contractions, list)), "Expected list for contractions variable."


xml_doc = get_xml_data(xml_raw_url)
input_text = "\n".join(xml_doc.xpath("//content/text()"))
del xml_doc



# --- Sampler section --- #
sample = input_text[:2000]
lines = list(map(lambda q: q.strip(), re.split(r"\s*\n\s*", sample)))


brackets_pattern: str = r"\([^\)]*\)"
brackets_p = re.compile(brackets_pattern, flags = re.I)

for line in lines:
    for w in contractions:
        if w in line:
            line = line.replace(w, "")

lines = [line for line in lines if not brackets_p.search(line)]









p = re.compile(r"", flags = re.I)
re.sub(r"([\W\S]+)", "", lines[0])


#  Clean up data
clean_pattern: str = r"\([^\)]*\)"
dialog_pattern: str = r"^([a-z ]+?:\s*)"
clean_input = re.sub(clean_pattern, "", input_text)


# Get dialog lines.
split_pattern: str = r"^(\w+)?:\s*(.+)"
p_split = re.compile(split_pattern, flags = re.M)
dialog_lines = p_split.findall(clean_input)

if dialog_lines:
    dialog_collection = []
    for line in dialog_lines:
#         tmp = " ".join(re.split(r"\s+", re.sub(r"([^\w]+)", " ", line.lower())))
        dialog_collection.append({"speaker": line[0], "phrase": line[1]})



phrase_collection = []
for line in dialog_lines:
    tmp = " ".join(re.split(r"\s+", re.sub(r"([^\w]+)", " ", line.lower())))
    phrase_collection.append({"phrase": tmp})


from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

sparkster = SparkSession.builder.appName("DialogRecommendr").getOrCreate()


df = sparkster.createDataFrame(dialog_collection)

if df:
    type(df)
    df.printSchema()




# https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.ml.recommendation.ALS.html

#TODO: Set user and items.

from pyspark.ml.recommendation import ALS

_als = ALS(maxIter=5, regParam=0.01, seed = 13)
_als.clear(_als.regParam)

train_pct: float = 0.8
df_training, df_test = df.randomSplit([train_pct, 1 - train_pct])


_als_mod = _als.fit(df_training)