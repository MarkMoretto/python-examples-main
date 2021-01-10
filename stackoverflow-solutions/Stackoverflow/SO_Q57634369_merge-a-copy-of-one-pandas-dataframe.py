
"""
Purpose: Replicate rows in dataframe and replicate smaller dataframe for each row of larger dataframe
Date created: 2019-08-23

Contributor(s):
    Mark M.

Ref: https://stackoverflow.com/questions/57634369/merge-a-copy-of-one-pandas-dataframe-into-every-row-of-another-dataframe/57634481#57634481
"""

"""
# output:
   a  b  id val
0  1  4  aa   a
1  1  4  bb   b
2  2  5  aa   a
3  2  5  bb   b
4  3  6  aa   a
5  3  6  bb   b
"""


import pandas as pd
big = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
small = pd.DataFrame({'id': ['aa','bb'], 'val':['a','b']})

small_len = len(small)


### Each dataframe replicates rows by the length of the other orgiinal dataframe
### The first one is ordered by the 'a' column, but you could adjust that
### Then the two dataframes are concatenated along hte column axis (1) to achieve the desired result.
def merge_expand(big, small):
    tmp_big = pd.concat([big] * len(small), ignore_index=True).sort_values(by=['a']).reset_index(drop=True)
    tmp_small1 = pd.concat([small] * len(big), ignore_index=True)
    return pd.concat([tmp_big, tmp_small1], 1)


merge_expand(big, small)


def merge_expand(*args):
    if len(args) == 2:
        if len(args[0]) > len(args[1]):
            df_1 = pd.concat([args[0]] * len(args[1]), ignore_index=True).sort_values(by=[args[0].columns[0]]).reset_index(drop=True)
            df_2 = pd.concat([args[1]] * len(args[0]), ignore_index=True)
            return pd.concat([df_1, df_2], 1)