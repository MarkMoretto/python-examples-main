
"""
Purpose: 
Date created: 2020-06-21

https://stackoverflow.com/questions/62500873/python-iteration-across-data-frames

Contributor(s):
    Mark M.
"""


import pandas as pd

sample = """
13-3-2020, A, 10, 15
13-4-2020, A, 11, 26
13-5-2020, A, 14, 14
2-2-2018, B, 10, 15
18-2-2018, B, 11, 26
5-4-2018, B, 14, 14
5-5-2018, B, 12, 12
""".strip()

tokens = sample.splitlines()
tdata = [tuple(t.split(",")) for t in tokens]

df_cols = ["Date", "Product", "Value1","Value2",]

df = pd.DataFrame(tdata, index=[i for i in range(len(tdata))], columns=["Date", "Product", "Value1","Value2",])


df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, infer_datetime_format=True)
df.loc[:, ["Value1", "Value2"]] = df.loc[:, ["Value1", "Value2"]].astype(int)
df["mth_start"] = df["Date"].apply(lambda x: f"{x.year}-{x.month}-1")
df["mth_start"] = pd.to_datetime(df["mth_start"])

df.sort_values(by=["Date", "Product"], ascending=[True, True], inplace=True)


df.groupby(["Product"])["Date"].min()
df.groupby(["Product"])["Date"].max()

(df.sort_values(by=['Date'], ascending=False).groupby(["Product"]).shift(1))

all_periods = pd.date_range(start=df["Date"].min(), end=df["Date"].max())

df2 = pd.DataFrame(index=[i for i in range(len(all_periods))], columns=["Date","mth_start"])
df2["Date"] =all_periods
df2["Date"] = pd.to_datetime(df2["Date"], infer_datetime_format=True)
df2.loc[:, "mth_start"] = df2.loc[:, "Date"].apply(lambda x: f"{x.year}-{x.month}-1")
df2.loc[:, "mth_start"] = pd.to_datetime(df2.loc[:, "mth_start"])


df3 = pd.merge(df2, df, how="outer", on=["Date", "mth_start"])

df4 = df3.iloc[:15,:].copy()
df4["new_date"]=pd.NaT

df4.loc[df4["Product"].isna(), "new_date"] = df4.loc[:, "mth_start"]
df4.loc[~df4["Product"].isna(), "new_date"] = df4.loc[:, "Date"]

mask = df4.where(df4["Product"].isna(), axis=1)

df4.mask(~df4["Product"].isna(), df4["mth_start"])
 df4.loc[:, ["Date","mth_start","Product"]]







