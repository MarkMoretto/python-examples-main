"""
Purpose: Solving a system of equations
Date created: 2020-03-13

Contributor(s):
    Mark M.

Solve:

  A - 4B + 2C = 16
 2A + 7B - 5C = 83
  A +  B -  C =  ?

"""

import numpy as np
import pandas as pd


ddict = dict(
        A=[ 1, 2],
        B=[-4, 7],
        C=[ 2, -5],
        D=[16, 83]
        )
df = pd.DataFrame(ddict)

# Find lowest common multiple for a column
X = df.loc[:, df.columns.values.tolist()[:-1]]
y = df.loc[:, df.columns.values.tolist()[-1]]


np.gcd.reduce(df["A"].values)

solve_for = "C"
lcm = np.lcm.reduce(df["A"].values)
match_idx = df[df["A"] == lcm].index
nonmatch_idx = df[df["A"] != lcm].index
if not match_idx is None:
    df.iloc[match_idx,:] = df.iloc[match_idx,:].apply(lambda x: x * -1)
    df.iloc[nonmatch_idx,:] = df.iloc[nonmatch_idx,:].apply(lambda x: x * lcm)
