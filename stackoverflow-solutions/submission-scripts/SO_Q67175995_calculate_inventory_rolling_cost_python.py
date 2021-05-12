
"""
Purpose: Stackoverflow
Date created: 2021-04-20

URL: https://stackoverflow.com/questions/67175995/calculate-inventory-rolling-cost-in-python

Note: I'm saving this mainly for unpacking of that dataset.

Contributor(s):
    Mark M.
"""

import pandas as pd

sample = """date	instrument	trade	quantity	price_net_local
2020-03-17	GS.YS	B	82000	123.3793038
2020-08-03	GS.YS	B	88000	133.1544325
2020-09-01	GS.YS	S	-151000	135.8211283
2020-10-09	GS.YS	B	144000	122.1733325
2020-12-01	GS.YS	S	-143000	128.410452
2021-01-04	GS.YS	B	143000	122.811284
2021-04-02	GS.YS	S	-138000	133.799
2021-04-15	GS.YS	S	-25000	118.0598442"""

lines = sample.split("\n")

cols = lines[0].split("\t")
col_map = {k:v for k, v in enumerate(cols)}


tmp = [line.split("\t") for line in lines[1:]]


ddict = dict.fromkeys(cols, None)
for i in range(len(cols)):
    ddict[col_map[i]] = [tmp[j][i] for j in range(len(tmp))]

df = pd.DataFrame(data = ddict)
df.loc[:, "quantity"] = df.loc[:, "quantity"].astype(int)
df.loc[:, "price_net_local"] = df.loc[:, "price_net_local"].astype(float)



df["tot_cost"] = df.loc[:, "quantity"] * df.loc[:, "price_net_local"]

(df.loc[df["trade"] == "B", "price_net_local"].cumsum() * df.loc[df["trade"] == "B", "quantity"].cumsum()) / df.loc[df["trade"] == "B", "quantity"]
df.loc[df["trade"] == "S", :]
(df.loc[df["trade"] == "B", "price_net_local"] / df.loc[df["trade"] == "B", "quantity"]).cumsum()