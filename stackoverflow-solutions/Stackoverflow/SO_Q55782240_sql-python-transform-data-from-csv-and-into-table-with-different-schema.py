
"""
Purpose: Reshape and load data to PostgreSQL.
Date: 2019-04-21
Contributor(s): Mark Moretto

URL: https://stackoverflow.com/questions/55782240/sql-python-transform-data-from-csv-and-into-table-with-different-schema-with-co/55782602#55782602
"""


import os
import pandas as pd
import datetime as dt

dir = r'C:\Users\Work1\Desktop\Portfolio_Stuff\Portfolio\Python\Stackoverflow'
csv_name = 'SO_Q55782240_Sample_SQL_Data.csv'
full_path = os.path.join(dir, csv_name)
data = pd.read_csv(full_path)

def process_df(dataframe=data):
    df1 = dataframe.copy(deep=True)
    df1['date_time'] = pd.to_datetime(df1['date_time'])
    df1['count'] = 1

    ### Maybe get unique types to list for future needs
    _types = df1['type'].unique().tolist()

    ### Process time-series shifts
    df1['start_time']  = df1['date_time'] - dt.timedelta(hours=1, minutes=0)
    df1['end_time']  = df1['date_time'] - dt.timedelta(hours=0, minutes=50)
    
    ## Create conditional masks for the dataframe
    pound_type = df1['type'] == 'pound'
    euro_type = df1['type'] == 'euro'

    ### Subsection each dataframe by currency; concatenate results
    df_p = df1[df1['type'] == 'pound']
    df_e = df1[df1['type'] == 'euro']
    df = pd.concat([df_p, df_e]).reset_index(drop=True)

    ### add conditional columns
    df['pound_cost'] = [x if x == 'pound' else 0 for x in df['type']]
    df['euro_cost'] = [x if x == 'euro' else 0 for x in df['type']]

    ### Manually input desired field arrangement
    fin_cols = [
        'id',
        'start_time',
        'end_time',
        'pound_cost',
        'euro_cost',
        'count',
        ]
    ### Return formatted dataframe
    return df.reindex(columns=fin_cols).copy(deep=True)

data1 = process_df()