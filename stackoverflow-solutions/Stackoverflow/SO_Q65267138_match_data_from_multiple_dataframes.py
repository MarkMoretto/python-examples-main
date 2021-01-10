
"""
Purpose: Stackoverflow answer
Date created: 2020-12-13

https://stackoverflow.com/questions/65267138/python-pandas-how-to-match-data-from-one-dataframe-to-another/65275924#65275924

Contributor(s):
    Mark M.
"""


import pandas as pd


"""
  Username Stock 1 Stock 2
0   JB3004    TSLA    MSFT
1   JM3009    SHOP    SPOT
2   DB0208    TWTR    MSFT
3   AB3011    TWTR    PTON
4   CB3004    MSFT    TSLA


               TWTR      SPOT      PTON      SHOP      MSFT      TSLA
Date           Adj Close Adj Close Adj Close Adj Close Adj Close Adj Close
2020-12-11     51.44     341.22     117.1   1057.87    213.26    609.99
"""

ddict1 = {
        "username": ["JB3004","JM3009","DB0208","AB3011","CB3004",],
        "Stock 1": ["TSLA","SHOP","TWTR","TWTR","MSFT",],
        "Stock 2": ["MSFT","SPOT","MSFT","PTON","TSLA",],
        }

ddict2 = {
        "TWTR": ["Adj Close", 51.44],
        "SPOT": ["Adj Close", 341.22],
        "PTON": ["Adj Close", 117.10],
        "SHOP": ["Adj Close", 1057.87],
        "MSFT": ["Adj Close", 213.26],
        "TSLA": ["Adj Close", 609.99],
        }

df1 = pd.DataFrame(ddict1)
df2 = pd.DataFrame(ddict2, index=["Date", "2020-12-11"])


df2t = df2.stack().reset_index().rename(
        columns={
                "level_0":"date",
                "level_1":"stock",
                0:"closing_price",
                },
        )

df2t = df2t.loc[df2t["date"] != "Date", :]


df1m = pd.melt(df1, id_vars=["username"], value_vars=["Stock 1", "Stock 2"])

df = pd.merge(df1, df2t, left_on=["Stock 1"], right_on=["stock"], sort=False)
df = pd.merge(df, df2t, left_on=["Stock 2"], right_on=["stock"], sort=False)



df = pd.merge(df1m, df2t, left_on="value", right_on="stock", sort=False)
df = df.drop("value", axis=1).rename(columns={"variable": "holding_id"})
df = df.pivot(index="username", columns="holding_id", values=["stock", "closing_price"]).rename(columns=lambda x: x.strip())


df.loc["AB3011","stock"]["Stock 1"]


df3 = pd.merge(df1, df2t, left_on=["Stock 1"], right_on=["stock"], sort=False)
df3 = pd.merge(df, df2t, left_on=["Stock 2"], right_on=["stock"], sort=False)


df = pd.merge(df1, df2t, left_on=["Stock 1"], right_on=["stock"], sort=False)
df = pd.merge(df, df2t, left_on=["Stock 2"], right_on=["stock"], sort=False)

