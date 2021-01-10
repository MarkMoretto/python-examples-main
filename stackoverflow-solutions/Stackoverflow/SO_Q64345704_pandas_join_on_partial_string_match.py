
"""
Purpose: Join by partial string
Date created: 2020-10-13

https://stackoverflow.com/questions/64345704/how-can-i-merge-a-pandas-dataframes-based-on-a-substring-from-one-of-the-columns#64345815

Contributor(s):
    Mark M.
"""


import re
import pandas as pd

ddict1 = {
        "School": ["Air Force", "Akron", "Alabama at Birmingham", "Auburn",],
        "Conference": ["Mt. West","MAC","C-USA","Sun Belt",],
        }

ddict2 = {
        "SCHOOL_NAME": ["Auburn University", "Air Force Academy", "Birmingham", "University of Akron",],
        "Rate": [93.0,53.0,75.0,77.0],
        }

df1 = pd.DataFrame(ddict1)
df2 = pd.DataFrame(ddict2)



df3 = df1["School"].apply(lambda x: df2["SCHOOL_NAME"].str.contains(x))
df4 = df2["SCHOOL_NAME"].apply(lambda x: df1["School"].str.contains(x))

df5 = pd.concat([df3, df4]).unstack(0).reset_index().rename(columns={"level_0":"df1","level_1":"df2",})
df1.loc[:, "index_match"] = df5.loc[df5[0]==True, "df2"].reset_index(drop=True)

df1.merge(df2, left_on="index_match", right_index=True).loc[:, ["School","Conference","Rate"]]

