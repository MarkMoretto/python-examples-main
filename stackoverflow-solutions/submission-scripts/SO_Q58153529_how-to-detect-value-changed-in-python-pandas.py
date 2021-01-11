
"""
Purpose: Stackoverflow: Detect value change in pandas dataframe column
Date created: 2019-09-29

Contributor(s):
    Mark M.

Ref: https://stackoverflow.com/questions/58153529/how-to-detect-value-changed-in-python-pandas-in-each-object
"""


import pandas as pd

# Provided data
raw_str = """
180762508,1268510763,374723980,293,20180402035748,198,25,1,1 180762508,1268503685,374717256,307,20180402035758,225,38,1,1 180762508,1268492506,374708540,236,20180402035808,222,52,1,1 180762508,1268485868,374697563,248,20180402035818,197,47,1,1 180762508,1268482430,374688520,272,20180402035828,196,31,1,1 180707764,1270608366,374988433,246,20180402035925,66,37,1,0 180707764,1270620899,374992366,222,20180402035935,68,49,1,0
"""

# Replace newline and split on single whitespace
chunks = raw_str.replace('\n', '').split(' ')

# Create simple dictionary for ID, timestamp, and interest columns
ddict = {}
ddict['id'] = [i.split(',')[0] for i in chunks]
ddict['timestamp'] = [i.split(',')[4] for i in chunks]
ddict['interest'] = [i.split(',')[-1] for i in chunks]

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(ddict)

# Create dictionary for sample data
# This is an existing ID with timestamp in the future and 1 as interest
tdict = {
        'id': '180707764',
        'timestamp': '20180402035945',
        'interest': '1',
        }
# Append that dictionary to your dataframe and sort by id, timestamp
df = df.append(pd.Series(tdict), ignore_index=True).copy(deep=True)
df = df.sort_values(['id', 'timestamp']).reset_index(drop=True)

# Shift dataframe back 1 period by rows
df2 = pd.DataFrame(df.shift(periods=-1, axis=0)

# Merge that dataframe with our original dataframe by index values
# We're dropping an extra id column and renaming our primary id column for aesthetics
df3 = df.merge(df2, left_index=True, right_index=True, suffixes=('_prev', '_curr'))
df3 = df3.drop('id_curr', axis=1).rename(columns={'id_prev': 'id'})


# Create a conditional to return the row where interest changed from 0 to 1
df3[(df3['interest_prev'] == '0') & (df3['interest_curr'] == '1')]

# You can also return specific columns by adding thos onto the end of the result set
df3[(df3['interest_prev'] == '0') & (df3['interest_curr'] == '1')]['timestamp_y']
df3[(df3['interest_prev'] == '0') & (df3['interest_curr'] == '1')][['id', 'timestamp_y']]


# Or, use iloc
df.iloc[df3[(df3['interest_prev'] == '0') & (df3['interest_curr'] == '1')].index, :]







# df.groupby(['id','timestamp', 'interest']).size()
# df1 = df.groupby(['id', 'interest']).size()


# df1 = df.groupby(['id', 'interest']).agg({'id': ['count'],'interest': ['count']})

# df2 = pd.DataFrame(df.shift(periods=-1, axis=0)

# df3 = df.merge(df2, left_index=True, right_index=True, suffixes=('_curr', '_next'))



# df.loc[]

# df[(df['interest'] == '0') & df['interest'] == '1')].count()
