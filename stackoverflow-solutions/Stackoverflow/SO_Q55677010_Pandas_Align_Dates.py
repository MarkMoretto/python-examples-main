
"""
Purpose: How to align data based on time?
Date created: 2019-04-15
Contributor(s): Mark Moretto

Ref: https://stackoverflow.com/questions/55677010/how-to-align-data-based-on-time/55691730#55691730
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

root = r'C:\Users\...\...'
file_name = 'SO_Q55677010_Align_Time.xlsx'
full_path = os.path.join(root, file_name)


### Import data
df = pd.read_excel(full_path)

### Get our switch columns
switch_cols = [i for i in df.columns.values.tolist() if i.startswith('switch')]

### Subset our main dataframe to include only switch columns
df1 = df.reindex(columns=switch_cols).copy()


def plot_results(dataframe):
    ### Get swtich column names into a list
    y_cols = [i for i in dataframe.columns.values.tolist()]

    ### Make the x-axis value set our dataframe axis values
    x_vals = dataframe.index.values.tolist()
    
    ### Create subplots based on the numer of swtich columns
    fig, axs = plt.subplots(len(y_cols), 1, sharex=True)

    ### Remove horizontal space between axes
    fig.subplots_adjust(hspace = 0)

    ### Iterate over enumerated list of switch columns
    for i, v in enumerate(switch_cols):
        ### set axes to plot values from a swtich set;
        ### Set drawstyle to 'steps-pre'
        axs[i].plot(x_vals, dataframe[v].values, drawstyle='steps-pre')

        ### Add padding to y-axis limits
        axs[i].set_ylim(-0.1, 1.1)

        ### Set y-axis label to switch column label
        axs[i].set_ylabel(v)

    ### Plot results
    plt.show()

plot_results(df1)




#import numpy as np

#df1['switch 2 shift'] = df1['switch 2'].shift(1)
#df1.loc[df1['switch 2 shift'].isna(), 'switch 2 shift'] = df1['switch 2']
#df1['switch 3 shift'] = df1['switch 3'].shift(1)

#def shift_cols(dataframe, temp_list=None):
#    df_x = dataframe.copy()

#    for i in df_x.columns.values.tolist():
#        tmp_name_st = i + ' start'
#        tmp_name_end = i + ' end'
#        df_x[tmp_name_st] = df_x[i]
#        df_x[tmp_name_end] = df_x[tmp_name_st].shift(1)
#        df_x.loc[df_x[tmp_name_end].isna(), tmp_name_end] = df_x[tmp_name_st]
#        df_x = df_x.drop(i, axis=1)

#    return df_x

#df2 = shift_cols(df1)
#df3 = df2.reindex(columns=[i for i in df2.columns.values.tolist() if i.endswith('start')])
#df4 = df2.reindex(columns=[i for i in df2.columns.values.tolist() if i.endswith('end')])

#ax = df3.plot()
#df4.plot(ax=ax)

#xyz = [i for i in df2.columns.values.tolist() if i.endswith('end')]