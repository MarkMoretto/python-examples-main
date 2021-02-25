
"""
Purpose: Stackoverflow Question
Date created: 2021-02-15

Title: Calculate how much of a trajectory/path falls in-between two other trajectories

URL: https://stackoverflow.com/questions/66166662/calculate-how-much-of-a-trajectory-path-falls-in-between-two-other-trajectories

Contributor(s):
    Mark M.
"""

import numpy as np
import pandas as pd

try:
    import pickle5 as pickle
except ModuleNotFoundError:
    print("Please install pickle5 and re-run script.")

from pathlib import Path

pd.set_option("display.width", 120)
pd.set_option("mode.chained_assignment", None)
pd.set_option("display.max_columns", None)


data_folder = Path(r"C:\Users\Work1\Desktop\Info\PythonFiles\stackoverflow-data\so-Q66166662-data")
pkl_dfh_name = "df_H.pickle"
pkl_dfr_name = "df_R.pickle"

with open(data_folder.joinpath(pkl_dfh_name), "rb") as ff:
    df_H = pickle.load(ff)

with open(data_folder.joinpath(pkl_dfr_name), "rb") as ff:
    df_R = pickle.load(ff)



# --- BEGIN: Provided Code --- #

df_R_cols = [
        '(0, 1, 1)_mean_X', '(0, 1, 1)_mean_Z',
        '(0, 1, 2)_mean_X', '(0, 1, 2)_mean_Z',
        '(0, 1, 3)_mean_X', '(0, 1, 3)_mean_Z',
        '(0, 2, 1)_mean_X', '(0, 2, 1)_mean_Z',
        '(0, 2, 2)_mean_X', '(0, 2, 2)_mean_Z',
        '(0, 2, 3)_mean_X', '(0, 2, 3)_mean_Z',
        '(1, 1, 1)_mean_X', '(1, 1, 1)_mean_Z',
        '(1, 1, 2)_mean_X', '(1, 1, 2)_mean_Z',
        '(1, 1, 3)_mean_X', '(1, 1, 3)_mean_Z',
        '(1, 2, 1)_mean_X', '(1, 2, 1)_mean_Z',
        '(1, 2, 2)_mean_X', '(1, 2, 2)_mean_Z',
        '(1, 2, 3)_mean_X', '(1, 2, 3)_mean_Z',
        '(2, 1, 1)_mean_X', '(2, 1, 1)_mean_Z',
        '(2, 1, 2)_mean_X', '(2, 1, 2)_mean_Z',
        '(2, 1, 3)_mean_X', '(2, 1, 3)_mean_Z',
        '(2, 2, 1)_mean_X', '(2, 2, 1)_mean_Z',
        '(2, 2, 2)_mean_X', '(2, 2, 2)_mean_Z',
        '(2, 2, 3)_mean_X', '(2, 2, 3)_mean_Z',
       ]

df_H_cols = [
        '(0, 1, 1)_top_X', '(0, 1, 1)_bottom_X',
        '(0, 1, 1)_top_Z', '(0, 1, 1)_bottom_Z',
        '(0, 1, 2)_top_X', '(0, 1, 2)_bottom_X',
        '(0, 1, 2)_top_Z', '(0, 1, 2)_bottom_Z',
        '(0, 1, 3)_top_X', '(0, 1, 3)_bottom_X',
        '(0, 1, 3)_top_Z', '(0, 1, 3)_bottom_Z',
        '(0, 2, 1)_top_X', '(0, 2, 1)_bottom_X',
        '(0, 2, 1)_top_Z', '(0, 2, 1)_bottom_Z',
        '(0, 2, 2)_top_X', '(0, 2, 2)_bottom_X',
        '(0, 2, 2)_top_Z', '(0, 2, 2)_bottom_Z',
        '(0, 2, 3)_top_X', '(0, 2, 3)_bottom_X',
        '(0, 2, 3)_top_Z', '(0, 2, 3)_bottom_Z',
        '(1, 1, 1)_top_X', '(1, 1, 1)_bottom_X',
        '(1, 1, 1)_top_Z', '(1, 1, 1)_bottom_Z',
        '(1, 1, 2)_top_X', '(1, 1, 2)_bottom_X',
        '(1, 1, 2)_top_Z', '(1, 1, 2)_bottom_Z',
        '(1, 1, 3)_top_X', '(1, 1, 3)_bottom_X',
        '(1, 1, 3)_top_Z', '(1, 1, 3)_bottom_Z',
        '(1, 2, 1)_top_X', '(1, 2, 1)_bottom_X',
        '(1, 2, 1)_top_Z', '(1, 2, 1)_bottom_Z',
        '(1, 2, 2)_top_X', '(1, 2, 2)_bottom_X',
        '(1, 2, 2)_top_Z', '(1, 2, 2)_bottom_Z',
        '(1, 2, 3)_top_X', '(1, 2, 3)_bottom_X',
        '(1, 2, 3)_top_Z', '(1, 2, 3)_bottom_Z',
        '(2, 1, 1)_top_X', '(2, 1, 1)_bottom_X',
        '(2, 1, 1)_top_Z', '(2, 1, 1)_bottom_Z',
        '(2, 1, 2)_top_X', '(2, 1, 2)_bottom_X',
        '(2, 1, 2)_top_Z', '(2, 1, 2)_bottom_Z',
        '(2, 1, 3)_top_X', '(2, 1, 3)_bottom_X',
        '(2, 1, 3)_top_Z', '(2, 1, 3)_bottom_Z',
        '(2, 2, 1)_top_X', '(2, 2, 1)_bottom_X',
        '(2, 2, 1)_top_Z', '(2, 2, 1)_bottom_Z',
        '(2, 2, 2)_top_X', '(2, 2, 2)_bottom_X',
        '(2, 2, 2)_top_Z', '(2, 2, 2)_bottom_Z',
        '(2, 2, 3)_top_X', '(2, 2, 3)_bottom_X',
        '(2, 2, 3)_top_Z', '(2, 2, 3)_bottom_Z',
        ]

# df_R = pd.DataFrame(np.random.randint(0,100,size=(1000, 36)), columns=df_R_cols)
# df_H = pd.DataFrame(np.random.randint(0,100,size=(1000, 72)), columns=df_H_cols)

"""
df_R contains the position data for the red paths (in X & Z).
Note that X & Z are both positional/spatial data. These data do not have a date/time-like
index.

df_H contains the position data for the black paths, which includes a 'top' and 'bottom'
column for X and for Z, corresponding to the two black paths in each plot.
"""


def CI_analysis(df_H, df_R):
    
    # separate X & Z 
    df_H_top_X = df_H.filter(regex='top_X')
    df_H_bottom_X = df_H.filter(regex='bottom_X')
    
    df_H_top_Z = df_H.filter(regex='top_Z')
    df_H_bottom_Z = df_H.filter(regex='bottom_Z')
    
    # df_R_X = CI_raycast.filter(regex='mean_X')
    # df_R_Z = CI_raycast.filter(regex='mean_Z')

    df_R_X = df_R.filter(regex='mean_X')
    df_R_Z = df_R.filter(regex='mean_Z')

    # check if X is within the range of top & bottom X
    CI_inside_X = pd.DataFrame()
    for col in df_R_X:
        temp = []
        c = 0
        for i, val in df_R_X[col].iteritems():
            if (val < df_H_top_X.iloc[i,c]) & (val > df_H_bottom_X.iloc[i,c]):
                temp.append(1)
            else: 
                temp.append(0)
        CI_inside_X[col] = temp
        c = c+1

    # check if Z is within the range of top & bottom Z
    CI_inside_Z = pd.DataFrame()
    for col in df_R_Z:
        temp = []
        # print(col)
        c = 0
        for i, val in df_R_Z[col].iteritems():
            if (val < df_H_top_Z.iloc[i,c]) & (val > df_H_bottom_Z.iloc[i,c]):
                temp.append(1)
            else: 
                temp.append(0)
        CI_inside_Z[col] = temp
        c = c+1

    # Check if X & Z were both in-between the top & bottom trajectories
    CI_inside = pd.DataFrame()
    for col in CI_inside_X:
        temp = []
        c = 0
        for i,row in CI_inside_X[col].iteritems(): 
            if (row == 1) & (CI_inside_Z.iloc[i,c] == 1):
                temp.append(1)
            else: 
                temp.append(0)
        CI_inside[col] = temp
        c = c+1
    
    CI_inside_avg = pd.DataFrame(CI_inside.mean(axis=0)).transpose() 
    
    return CI_inside_X, CI_inside_Z, CI_inside, CI_inside_avg

# --- END: Provided Code --- #

# df_R = pd.DataFrame(np.random.randint(0, 100, size=(1000, 36)), columns=df_R_cols)
# df_H = pd.DataFrame(np.random.randint(0, 100, size=(1000, 72)), columns=df_H_cols)

a_rng = range(3)
b_rng = range(1, 3)
c_rng = range(1, 4)
all_my_tuples = [(a, b, c) for a in a_rng for b in b_rng for c in c_rng]

# df_R_cols = [f"({a}, {b}, {c})_mean_{e}" for a in a_rng for b in b_rng for c in c_rng for e in ["X","Z",]]
df_R_cols = [f"{x}_mean_{e}" for x in all_my_tuples for e in ["X","Z",]]
df_H_cols = [f"{x}_{pos}_{e}" for x in all_my_tuples for e in ["X","Z",] for pos in ["top", "bottom",]]

# [f"({a}, {b}, {c})_{pos}_{e}" for a in range(3) for b in range(1, 3) for c in range(1, 4) for e in ["X","Z",] for pos in ["top", "bottom",]]



# separate X & Z
# df_H_top_X = df_H.filter(regex='top_X')
# df_H_bottom_X = df_H.filter(regex='bottom_X')

# df_H_top_Z = df_H.filter(regex='top_Z')
# df_H_bottom_Z = df_H.filter(regex='bottom_Z')

# df_R_X = df_R.filter(regex='mean_X')
# df_R_Z = df_R.filter(regex='mean_Z')

# Create huge dataframe
df_R_H = pd.merge(df_R, df_H, left_index=True, right_index=True)

### Testing ###

# Comments -
#  for some reason X & Z are the equivalent of Y & X

#  Top and Bottom 'switch' sometimes for different groups (i.e, (0,1,3) vs (2,2,3).
#  However, within each group, they do not swtich.

# df_011 = df_R_H.loc[:, ["(0, 1, 1)_top_X", "(0, 1, 1)_mean_X", "(0, 1, 1)_bottom_X", "(0, 1, 1)_top_Z", "(0, 1, 1)_mean_Z", "(0, 1, 1)_bottom_Z"]]
# df_011.query("(`(0, 1, 1)_mean_X` < `(0, 1, 1)_top_X` & `(0, 1, 1)_mean_X` > `(0, 1, 1)_bottom_X`) & (`(0, 1, 1)_mean_Z` < `(0, 1, 1)_top_Z` & `(0, 1, 1)_mean_Z` > `(0, 1, 1)_bottom_Z`)")


df_013 = df_R_H.loc[:, ["(0, 1, 3)_top_X", "(0, 1, 3)_mean_X", "(0, 1, 3)_bottom_X", "(0, 1, 3)_top_Z", "(0, 1, 3)_mean_Z", "(0, 1, 3)_bottom_Z"]]
# res_df = df_013.query("(`(0, 1, 3)_mean_X` < `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` > `(0, 1, 3)_bottom_X`) & (`(0, 1, 3)_mean_Z` < `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` > `(0, 1, 3)_bottom_Z`)")
# res_df = df_013.query("(`(0, 1, 3)_mean_X` > `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` < `(0, 1, 3)_bottom_X`) & (`(0, 1, 3)_mean_Z` > `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` < `(0, 1, 3)_bottom_Z`)")

# res_df = df_013.query("`(0, 1, 3)_mean_X` > `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` < `(0, 1, 3)_bottom_X`")
# res_df = df_013.query("`(0, 1, 3)_mean_X` < `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` > `(0, 1, 3)_bottom_X`")

# res_df = df_013.query("(`(0, 1, 3)_mean_Z` < `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` > `(0, 1, 3)_bottom_Z`) or (`(0, 1, 3)_mean_Z` > `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` < `(0, 1, 3)_bottom_Z`)")
# res_df = df_013.query("(`(0, 1, 3)_mean_Z` > `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` < `(0, 1, 3)_bottom_Z`)")



df_013_a = df_013.query("((`(0, 1, 3)_mean_X` < `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` > `(0, 1, 3)_bottom_X`) or (`(0, 1, 3)_mean_X` > `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` < `(0, 1, 3)_bottom_X`))")
df_013_a = df_013.query("(`(0, 1, 3)_mean_X` < `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` > `(0, 1, 3)_bottom_X`) or (`(0, 1, 3)_mean_X` > `(0, 1, 3)_top_X` & `(0, 1, 3)_mean_X` < `(0, 1, 3)_bottom_X`)")
df_013_b = df_013.query("((`(0, 1, 3)_mean_Z` < `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` > `(0, 1, 3)_bottom_Z`) or (`(0, 1, 3)_mean_Z` > `(0, 1, 3)_top_Z` & `(0, 1, 3)_mean_Z` < `(0, 1, 3)_bottom_Z`))")


df_013.loc[:, ['(0, 1, 3)_top_X', '(0, 1, 3)_mean_X', '(0, 1, 3)_bottom_X',]].plot(kind="line")
df_013.loc[:, ['(0, 1, 3)_top_Z', '(0, 1, 3)_mean_Z', '(0, 1, 3)_bottom_Z',]].plot(kind="line")

# Create output dataframe using all_my_tuples as index
df_fin = pd.DataFrame(index = map(str, all_my_tuples), columns=["n_found",])

# Iterate tuple elements
for t in all_my_tuples[:3]:
    # Create query list.
    qry_parts = []
    qry_B = []
    # Repeat same query creation process for X and Z.
    for xz in ["X", "Z"]:
        qry_string = f"(`{t}_mean_{xz}` < `{t}_top_{xz}` & `{t}_mean_{xz}` > `{t}_bottom_{xz}`)"
        qry_string += f" or (`{t}_mean_{xz}` > `{t}_top_{xz}` & `{t}_mean_{xz}` < `{t}_bottom_{xz}`)"
        qry_parts.append(f"({qry_string})")
        # qry_A.append(f"(`{t}_mean_{xz}` < `{t}_top_{xz}` & `{t}_mean_{xz}` > `{t}_bottom_{xz}`)")
        # qry_B.append(f"(`{t}_mean_{xz}` > `{t}_top_{xz}` & `{t}_mean_{xz}` < `{t}_bottom_{xz}`)")

    # Join to create full query and execute into new dataframe
    qry = " & ".join(qry_parts)
    print(qry + "\n")
    dft = df_R_H.query(qry)

    # Update dataframe with row count
    if not (dft) is None:
        df_fin.loc[f"{t}", "n_found"] = dft.shape[0]
    else:
        df_fin.loc[f"{t}", "n_found"] = 0

# Then divide by the row count of one of the dataframes.
df_fin["n_mean"] = df_fin.loc[:, "n_found"].apply(lambda q: q / df_R.shape[0])







