
"""
Purpose: 
Date created: 2020-03-09

Contributor(s):
    Mark M.
"""
import re
import pandas as pd
from scipy.signal import find_peaks

sample = """
216.8099976     216.3399963
215.1499939     213.2299957
214.6999969     213.1499939
215.7299957     215.2799988
213.6900024     213.3699951
214.8800049     213.4100037
214.5899963     213.4199982
216.0299988     215.8200073
217.5299988     217.1799927
216.8800049     215.9900055
215.2299957     214.2400055
215.6799927     215.5700073
""".strip()

lines = sample.split("\n")

ddict = dict(High=[], Low=[])
for line in lines:
    tmp = re.split(r"\s+", line)
    ddict["High"].append(tmp[0])
    ddict["Low"].append(tmp[1])

df = pd.DataFrame(ddict)
for c in df.columns:
    df[c] = df[c].astype(float)


# Grab the minimum value for all highs
min_high = df["High"].min()

peaks, _ = find_peaks(df["High"], height=min_high)
peaks_df = df.loc[peaks, "High"].to_frame().rename(columns={"High":"local_high"})

df1 = df.merge(peaks_df, how="left", left_index=True, right_index=True)
df1.loc[~df1["local_high"].isna(), "local_high"] = 1
df1.loc[df1["local_high"].isna(), "local_high"] = 0
df1["local_high"] = df1["local_high"].astype(int)

df1.loc[df1["local_high"] != 0., "local_high"] = 1.

df.loc[3, "High"].diff()


df["High_lead_1"] = df["High"].shift(periods=-1,axis=0)
df["High_lead_2"] = df["High"].shift(periods=-2,axis=0)
df["High_lag_1"] = df["High"].shift(periods=1,axis=0)
df["High_lag_2"] = df["High"].shift(periods=2,axis=0)

df1 = df.drop("Low", axis=1)
df1["High"].diff()