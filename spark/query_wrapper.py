
import re
import pandas as pd
from functools import wraps

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from py4j.protocol import Py4JJavaError # To handle local testing errors
from pyspark.sql.utils import AnalysisException


def query_view(func):
    def inner(*args, **kwargs):
        # Try and grab view name from query.
        query = func(*args, **kwargs)

        sql_pattern = r"(?:\n|\s)?FROM\s([a-z0-9_]+)(?:\n|\s)?"
        res = re.search(sql_pattern, query, flags=re.I)
        if res:
            vw_nm = res.group(1)

        df.createOrReplaceTempView(vw_nm)
        spark.sql(query).show()
        spark.catalog.dropTempView(vw_nm)

    return inner



# Takes an optional `view_name` argument
def query_view_df(func):
    def inner(*args, **kwargs):
        '''
        Args should include `query` and `dataframe` objects.
        '''
        query, df = func(*args, **kwargs)

        sql_pattern = r"(?:\n|\s)?FROM\s([a-z0-9_]+)(?:\n|\s)?"
        res = re.search(sql_pattern, query, flags=re.I)
        if res:
            vw_nm = res.group(1)

        df.createOrReplaceTempView(vw_nm)
        spark.sql(query).show()
        spark.catalog.dropTempView(vw_nm)
    return inner





@query_view
def run_query(query_string=None):
    if not query_string is None:
        return query_string.strip()


@query_view_df
def run_query_df(query_string=None, dataframe=None):
    '''Same as run_query, but with dataframe param for some flexibility.'''
    return query_string.strip(), dataframe


qry = """
SELECT CAR_LINE_ICD9_DGNS_CD,
CAR_LINE_HCPCS_CD,
CAR_LINE_BETOS_CD,
CAR_LINE_CMS_TYPE_SRVC_CD
FROM vwdf
LIMIT 10
"""
run_query_df(qry, df)
