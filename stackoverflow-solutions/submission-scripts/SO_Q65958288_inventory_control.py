
"""
Purpose: 
Date created: 2021-01-29
https://stackoverflow.com/questions/65958288/python-solve-complex-inventory-in-dataframe
Contributor(s):
    Mark M.
"""
import re
from io import StringIO
import pandas as pd

pd.set_option("mode.chained_assignment", None)
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)

sample = """
Inventory count Batch size  Store A needs   Store B needs   Store C needs    Total requires       Actually requires
198      20             63               18             104           185                   220
876     100            567              435             673          1675                  1800
1759       6           1212              758             836          2806                  2814
2000    1000            333              444             555          1332                  3000
""".strip()

index_values = ["Buckets", "Candy Bars", "Coke (cans)", "Masks (boxes)",]

data = sample.split("\n")
cols = data[0]
cols = re.sub(r"(\s+)(?=[A-Z][a-z]+)", ",", cols)

data = data[1:]
data = [cols] + [re.sub(r"\s+", ",", line) for line in data]
# print("\n".join(data))

s = StringIO("\n".join(data))
df = pd.read_csv(s)

# data = sample.split("\n")
# colst = data[0]
# colst = re.sub(r"(\s+)(?=[A-Z][a-z]+)", "\t", colst)
# datat = data[1:]
# datat = [colst] + [re.sub(r"\s+", "\t", line) for line in datat]

required = lambda value, batch_sz: batch_sz - (value % batch_sz)

denom=df.loc["Buckets", ["Store A needs","Store B needs","Store C needs"]].sum()
df.loc["Buckets", ["Store A needs","Store B needs","Store C needs"]] / denom

df.loc["Buckets", "Store A needs"]