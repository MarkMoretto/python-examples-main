
"""
Purpose: Stackoverflow question: Combining and outputting multiple columns to csv
Date created: 2019-12-22

URI: https://stackoverflow.com/questions/59445183/how-to-combine-datafame-column-data-and-fixed-text-string/59445535#59445535

Contributor(s):
    Mark M.
"""


import pandas as pd

# Sample data, split by whitespace
sample = 'name1 476912.131 6670122.28567 470329.94956 6676260.27134 4861584.31433 wind1 wave1'
data = sample.split()

# Given column names
columns=['Name','SOLE','SOLN','EOLE','EOLN','EOLKP','Wind','Wave']

# Temp dictionary for converting to dataframe
ddict = dict(zip(columns, data))

df=pd.DataFrame(ddict, index=[0])

# Set as float data type
float_cols = ['SOLE','SOLN','EOLE','EOLN','EOLKP',]
df[float_cols] = df[float_cols].astype(float)



#### Needs comma, not space, between SOLN and EOLE

# Columns to format and output
target_cols = ['SOLE','SOLN','EOLE','EOLN',]

comma_col = 'SOLN'
last_col = df[target_cols].columns.values.tolist()[-1]
for col in df[target_cols]:
    if col == comma_col:
        df[col] = df[col].apply(lambda x: f"{x:.3f},")
    elif col == last_col:
        df[col] = df[col].apply(lambda x: f"{x:.3f}")
    else:
        df[col] = df[col].apply(lambda x: f"{x:.3f}" + " ")

# Result
df['WKT'] = df[target_cols].apply(lambda x: \'(LINESTRING ' \
  + ''.join(i for i in x) + \
  ')', axis=1)





