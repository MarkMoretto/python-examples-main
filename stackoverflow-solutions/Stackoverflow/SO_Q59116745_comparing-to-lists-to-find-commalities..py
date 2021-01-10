
"""
Purpose: SO - Find common column values based on another column
Date created: 2019-11-30
URI: https://stackoverflow.com/questions/59116745/find-common-column-values-based-on-another-column/59117340#59117340

Contributor(s):
    Mark M.
"""

import pandas as pd

df = pd.DataFrame({'userId' : [1,2,3,1,3,6,2,4,1,2], 'movieId' : [222,222,900,555,555,888,555,222,666,666]})

n_common = 3
n_users = 2

df1 = df.groupby('userId')['movieId'].apply(list).reset_index(name='movies')

# Get those with the number of common movies
df2 = df1.loc[df1['movies'].apply(lambda x: len(x))== n_common,:]

# Explode results
df3 = df2.explode('movies')

# Get viewer count per common movie.
df4 = df3.groupby('movies').size().reset_index(name='viewer_count')


if len(df4[df4['viewer_count'] == n_users]) ==n_common:
    tmp = '\n\t'.join([str(i) for i in list(set(df3['userId']))])
    print(f'Users with three common movies: \n\t{tmp}')
