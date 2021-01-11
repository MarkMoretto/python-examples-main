
"""
Ref: https://stackoverflow.com/questions/55705910/reformatting-a-sequential-data-file-into-a-data-frame-using-pandas

I have an input file, now converted to a pandas.dataframe. The records/rows are in a sequence which contain related data of the form

    survey, a, b, c
    section, 1, 2, 3
    observation, a, b, c
    values, 1, 2, 3 
    values, 4, 5, 6
    observation, d, e, f
    values, 7, 8, 9
    section, 4, 5, 6
    ...
The survey record only occurs once. A section may occur multiple times and will contain observation and value records. Observations will always be followed by values sometimes as multiple records.

I am trying to reformat this into rows where each set of values is on a separate row with its corresponding survey, section, and observation.

survey, a,b,c, section, 1,2,3, observation, a,b,c, values, 1,2,3
survey, a,b,c, section, 1,2,3, observation, a,b,c, values, 4,5,6
survey, a,b,c, section, 1,2,3, observation, d, e, f, values, 7, 8, 9
survey, a,b,c, section, 4, 5, 6 and so on....


Can this be done with pandas or should I iterate through an if, then else structure ?

The methods I've tried so far are the following (these are probably simplistic and heading in the wrong directions):

#pd.DataFrame(hmdDataToProcess.unstack())
#hmdDataToProcess.unstack
#hmdDataToProcess.stack

#pd.melt(hmdDataToProcess, id_vars =[0], value_vars = 
['SURVEY','SECTION','OBSERV','OBVAL'])

#df2 = hmdDataToProc0ess.pivot_table(index = [0]).reset_index()

#df2 = df_in.pivot_table(index = 
#['Example1','Example2'],columns='VC', values=
#['Weight','Rank']).reset_index()

#hmdDataToProcess.groupby('SECTION').groups #, 'OBSERV', 'OBVAL'

"""


import pandas as pd
import numpy as np

ddict = {
    'name':['survey','section','observation','values','values','observation','values','section',],
    'value1':['a','1','a','1','4','d','7','4',],
    'value2':['b','2','b','2','5','e','8','5',],
    'value3':['c','3','c','3','6','f','9','6',],
    }

rank_dict = {
    'survey': '1',
    'section': '2',
    'observation': '3',
    'values': '4',
    }

df = pd.DataFrame(ddict)
df['value key'] = df['name'].map(rank_dict)

df['row number'] = df.sort_values(['name','value1','value2','value3',]).groupby(['name']).cumcount() + 1
new_cols = ['row number','value key', 'name','value1','value2','value3',]
df = df.reindex(columns=new_cols)
df = df.sort_values(['row number','value key'], ascending=[True, True]).copy(deep=True)
df['combined'] = df['name'] + ',' + df['value1'] + ',' + df['value2'] + ',' + df['value3']

df1 = df.drop(['name','value1','value2','value3',], axis=1).copy().reset_index(drop=True)
#df1['combo_rank'] = df1['row number'].astype(str) + df1['value rank'].astype(str)

df3 = df2.stack()
df4 = df3.unstack(0)


pd.melt(df1, id_vars=[('row number', 'value key')], value_vars=['combined'])


col_dict = {
    '1':'SURVEY',
    '2':'SECTION',
    '3':'OBSERV',
    '4':'OBVAL',
    }

def unpivot(frame):
    N, K = frame.shape
    data = {'value': frame.to_numpy().ravel('F'),
            'variable': np.asarray(frame.columns).repeat(N),
            'date': np.tile(np.asarray(frame.index), K)}
    return pd.DataFrame(data, columns=[i for i in col_dict.values()])



col_dict = {
    '1':'SURVEY',
    '2':'SECTION',
    '3':'OBSERV',
    '4':'OBVAL',
    }
df2 = pd.DataFrame(columns=[i for i in col_dict.values()])
df2 = pd.DataFrame()
for i in df1.index.values.tolist():
    if df1['value id'][i] == k:
        rn = df1['row number'][i]
        tmp_val = df1['combined'][i]

        #print(v, ' - ', rn, ': ', tmp_val)
        df2[v][rn-1] = tmp_val
        print(k, ': ', v, ', Index: ', i, ' Value: ', df1['combined'][i])

        print(df1['value rank'][i], ' - ', df1['combined'][i])


pd.pivot_table(df, values=['combined'], index=['row number',], columns=['value rank'])
df.pivot(index=['row number'], columns=['value rank'], values=['combined'])