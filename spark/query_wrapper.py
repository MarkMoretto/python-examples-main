
import re
from pyspark.sql import dataframe

# Regular expression for basic SQL parsing.
# Aim is to capture name of dataframe view.
SQL_PATTERN: str = r"""
    (?:\n|\s)?
    FROM\s([a-z0-9_]+)
    (?:\n|\s)?
    """

# Compile regex pattern with flags.
p = re.compile(SQL_PATTERN, flags = re.I | re.X)



def query_view(func):
    """Simple decorator for basic Spark sql query views.
    """    
    def inner(*args, **kwargs):
        # Try and grab view name from query.
        
        _query: str = None
        _viewname: str = ""

        if len(args) == 1:
            _query = args[0]
            if not isinstance(_query, str):
                raise ValueError("String data type expected.")

            res = p.search(_query)
            if res:
                _viewname = res.group(1)

            df.createOrReplaceTempView(_viewname)
            spark.sql(_query).show()
            spark.catalog.dropTempView(_viewname)

    return inner



def query_view_df(func):
    """Simple decorator for basic Spark sql query views.
    
    Similar to `query_view`, but this wrapper allows for passing of
    DataFrame object.
    """
    def inner(*args, **kwargs):
        """Args list should include a query string and pandas.DataFrame objects.
        """
        _query: str = None
        _df = None
        _viewname: str = ""
            
        # Check argument count
        if len(args) == 2:
            # Assert data type of one argument
            # Set variables accordingly.
            if isinstance(args[0], str):
                _query = args[0]
                _df = args[1]
            else:
                _df = args[0]
                _query = args[1]
            
            # Quick validation.
            assert isinstance(_query, str), "String expected."
            assert isinstance(_df, dataframe.DataFrame), "PySpark.sql.dataframe.DataFrame expected."

            
            # Search for viewname within SQL query.
            # If found, update _viewname variable.
            res = p.search(_query)
            if res:
                _viewname = res.group(1)

            # Create temporary view, run SQL, destroy temporary view.
            _df.createOrReplaceTempView(_viewname)
            spark.sql(_query).show()
            spark.catalog.dropTempView(_viewname)
            
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
