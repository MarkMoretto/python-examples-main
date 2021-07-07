

# https://stackoverflow.com/questions/68261345/pandas-drop-and-update-rows-and-columns-based-on-column-value
"""
when "wide" or "noball" is null, crun = crun + run + extra until ball = 0.1 (recursively)
when "wide" or "noball" is not null, concurrent ball value won't be incremented
and will be dropped after crun calculation. crun = crun + run + extra.
And it will continue until ball = 0.1 (recursively) eg. Let me breakdown:
from row index 0 to 8:
    | 0.1 "wide" or "noball" is null and crun = 1
    | 0.2 "wide" or "noball" is null and crun = 1+4 =5
    | 0.3 "wide" or "noball" is not null (removed)
    | 0.4 "wide" or "noball" is null (becomes 0.3) and crun = 5+1+5+1 = 12
    | 0.5 "wide" or "noball" is not null (removed)
    | 0.6 "wide" or "noball" is null (becomes 0.4) and crun = 12+1+1+2+1 = 17
    | 0.7 "wide" or "noball" is not null (removed)
    | 0.8 "wide" or "noball" is null (becomes 0.5) and crun = 17+6+2 = 25
    | 0.9 "wide" or "noball" is null (becomes 0.6) and crun = 25+1+1 =27

Finally "total" column will be created which returns the max of crun until 
ball = 0.1 (recursively). Then "run", "extra", "wide", "noball" column should
be dropped.

# Scoring: there is a rule in Cricket match each over consists of 6 consecutive legal balls. Whereas "wide" and "noball" are illegal.
# That's why illegal balls should be removed and reindex the ball values.

Expected output - 

  venue ball  crun total
0   a   0.1     1   45
1   a   0.2     5   45
2   a   0.3     12  45
3   a   0.4     17  45
4   a   0.5     25  45
5   a   0.6     27  45
6   a   1.1     31  45
7   a   1.2     32  45
8   a   1.3     39  45
9   a   1.4     42  45
10  a   1.5     44  45
11  a   1.6     45  45
12  a   0.1     5   27
13  a   0.2     9   27
14  a   0.3     11  27
15  a   0.4     14  27
16  a   0.5     14  27
17  a   0.6     23  27
18  a   1.1     27  27
"""

import re
import pandas as pd
raw_data = """
venue   ball    run     extra   wide    noball
a       0.1     0       1       NaN     NaN
a       0.2     4       0       NaN     NaN
a       0.3     1       5       5.0     NaN
a       0.4     1       0       NaN     NaN
a       0.5     1       1       NaN     1.0
a       0.6     2       1       NaN     NaN
a       0.7     6       2       1.0     1.0
a       0.8     0       0       NaN     NaN
a       0.9     1       1       NaN     NaN
a       1.1     2       2       NaN     NaN
a       1.2     1       0       NaN     NaN
a       1.3     6       1       NaN     NaN
a       1.4     0       2       NaN     2.0
a       1.5     1       0       NaN     NaN
a       1.6     2       0       NaN     NaN
a       1.7     0       1       NaN     NaN
a       0.1     0       5       NaN     NaN
a       0.2     4       0       NaN     NaN
a       0.3     1       1       NaN     NaN
a       0.4     3       0       NaN     NaN
a       0.5     0       0       NaN     NaN
a       0.6     0       2       2.0     NaN
a       0.7     6       1       NaN     NaN
a       1.1     4       0       NaN     NaN
""".strip()

lines = []
for line in raw_data.split("\n"):
    lines.append(re.sub(r"(\s+|\t)", "`", line))
headers = {k:v for k, v in enumerate(lines[0].split("`"))}
content = [["" if j == "NaN" else j for j in i.split("`")] for i in lines[1:]]

df = pd.DataFrame(data = content, columns = headers.keys())
df.rename(columns = headers, inplace = True)
df[["run", "extra",]] = df[["run", "extra",]].astype(int)
df.loc[df["wide"]=="", "wide"] = None
df.loc[df["noball"]=="", "noball"] = None
df[["ball", "wide", "noball"]] = df[["ball", "wide", "noball"]].astype(float)


# Create target groupings by ball value.
df["target_groups"] = df.loc[df["ball"] == 0.1].groupby(level=-1).ngroup()
df["target_groups"].fillna(method="ffill", inplace=True)


# Create subgroups
df["target_subgroups"] = df["ball"].astype(int)


# # For ball renumbering
# df["over_groups"] = 0.1
# df.loc[df["ball"].astype(int) < 1, "over_groups"] = 0.1
# df.loc[df["ball"].astype(int) >= 1, "over_groups"] = 1.1
# df.groupby(["target_groups","over_groups"]).cumsum()

# Add field fro sum of run and extra
df["run_extra"] = df[["run", "extra"]].sum(axis=1)

# Apply groupby() and cumsum() as follows to get the cumulative sum
# of each ball group for run and extra.
df["crun"] = df.groupby(["target_groups"])["run_extra"].cumsum()

# Create dataframe for max crun value of each group
group_max_df = df.groupby(["target_groups"])["crun"].max().to_frame().reset_index()

# Merge both of the DataFrames with the given suffixes.  The first one
# Just prevents crun from having a suffix added, which is an additional
# step to remove.
# You could probably use .join() in a similar manner.
df = pd.merge(df, group_max_df,
    on=["target_groups"],
    suffixes=("", "_total"),
    sort=False
)
# Rename your new total field.
df.rename(columns={"crun_total": "total"}, inplace = True)

# Apply your wide and noball condition here.
df = df.loc[(df["wide"].isna()) & (df["noball"].isna()), :].copy()


# Reset ball column
df["tmp_ball"] = 0.1
df.loc[:, "ball"] = df.groupby(["target_subgroups"])["tmp_ball"].cumsum() % 0.6
df.loc[df["ball"] == 0.0, "ball"] = 0.6
df["ball"]  = df["ball"] + df["target_subgroups"]




# df.loc[(df["wide"].isna()) & (df["noball"].isna()), :]
# df.loc[(df["wide"].notna()) | (df["noball"].notna()), "ball"].shift(periods = -1)
# df.loc[(df["wide"].isna()) & (df["noball"].isna()), "ball"].shift(periods = -1)
# df["ball"]
# df2["ball"]
# df2["ball"].diff()

# Reset your main index, if desired
df.reset_index(drop=True, inplace=True)

# Select only desired field for output.
df = df.loc[:, ["venue","ball","crun","total"]]


# df1["cumul_run"] = df1["run_extra"].cumsum()


# df1[["wide", "noball"]].diff(axis=1) # XOR
# df1 = df1[(df1["wide"].isna()) & (df1["noball"].isna())].copy()

# Partition by "ball" == 0.1
# df1["target_groups"] = df1.loc[df1["ball"] == 0.1].groupby(level=-1).ngroup()
# df1["target_groups"].fillna(method="ffill", inplace=True)

# df1["crun"] = df1.groupby(["target_groups"])["run_extra"].cumsum()



"""
  venue ball  crun total
0   a   0.1     1   45
1   a   0.2     5   45
2   a   0.3     12  45
3   a   0.4     17  45
4   a   0.5     25  45
5   a   0.6     27  45
6   a   1.1     31  45
7   a   1.2     32  45
8   a   1.3     39  45
9   a   1.4     42  45
10  a   1.5     44  45
11  a   1.6     45  45
12  a   0.1     5   27
13  a   0.2     9   27
14  a   0.3     11  27
15  a   0.4     14  27
16  a   0.5     14  27
17  a   0.6     23  27
18  a   1.1     27  27
"""
