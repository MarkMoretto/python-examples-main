
"""
Purpose: Stackoverflow answer
Date created: 2021-01-09

URL: https://stackoverflow.com/questions/65643483/bokeh-plot-is-empty/65643667#65643667

Contributor(s):
    Mark M.
"""


import re
import pandas as pd
import bokeh

sample = """
2018-10-22  7468.629883 2.282400e+09 0.263123    NASDAQ
2018-10-23  7437.540039 2.735820e+09    -0.416272   NASDAQ
2018-10-24  7108.399902 2.935550e+09    -4.425390   NASDAQ
2018-10-25  7318.339844 2.741810e+09    2.953406    NASDAQ
2018-10-26  7167.209961 2.964780e+09    -2.065084   NASDAQ
""".strip()


lines = [re.split(r"\s+", line) for line in sample.split("\n")]
df = pd.DataFrame(data=lines)
df.columns = ["Date","Adj Close","Volume","Day_Perc_Change","Name"]

df.loc[: , "Date"] = pd.to_datetime(df.loc[: , "Date"], infer_datetime_format = True)
df.loc[: , "Adj Close"] = df.loc[: , "Adj Close"].astype(float)