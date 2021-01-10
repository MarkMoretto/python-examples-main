
"""
Purpose: 
Date created: 2019-12-26

URI: https://stackoverflow.com/questions/59489368/pandas-return-separate-dataframe-values-based-on-function/59490607#59490607

Contributor(s):
    Mark M.
"""
import re
import pandas as pd

def x_abs(a: int) -> int:
    return a if a >=0 else a*(-1)

df1 = pd.DataFrame({'Lat' : [30, 37, 54, 67],
                    'Long' : [31, 48, 62, 63]})

df2 = pd.DataFrame({'Station_Lat' : [30, 43, 84, 67],
                    'Station_Long' : [32, 48, 87, 62],
                    'Station':['ABC', 'DEF','GHI','JKL']})

df3 = pd.merge(df1, df2, on='key')
df3[['Lat','Station_Lat',]] = df3[['Lat','Station_Lat',]].astype(int)

df3[df3.apply(lambda x, col1='Lat', col2='Station_Lat': x[col1]-x[col2] >= -1 and x[col1]-x[col2] <= 1, axis=1)]['Station']

df3[df3.apply(lambda x, col1='Lat', col2='Station_Lat': ((x_abs(x[col1]-x[col2])^1)>=1), axis=1)]['Station']
df3[(((x['Lat']-x['Station_Lat']^-1)>=-1) & ((x['Lat']-x['Station_Lat']^-1)>=-1))]


for i in df1.index:
    for j in df2.index:
        if abs(df1.loc[i, 'Lat'] - df2.loc[j, 'Station_Lat']) <=1:
            print(df2.loc[j, 'Station'])

df2.loc[i for i in df1.index for j in df2.index if abs(df1.loc[i, 'Lat'] - df2.loc[j, 'Station_Lat']) <=1, 'Station']



df1['loc_bucket'] = df1.index

# Naive approach
df1_lat_min = df1['Lat'].min()
df1_lat_max = df1['Lat'].max()
df1_long_min = df1['Long'].min()
df1_long_max = df1['Long'].max()


df2_lat_min = df2['Station_Lat'].min()
df2_lat_max = df2['Station_Lat'].max()
df2_long_min = df2['Station_Long'].min()
df2_long_max = df2['Station_Long'].max()


print(f"Coordinate latitude, min: {df1_lat_min}, max: {df1_lat_max}")
print(f"Station latitude, min: {df2_lat_min}, max: {df2_lat_max}")


df2.loc[df2['Station_Lat'].apply(lambda x: abs(x-df3['Lat'])<=1), 'Station']

list(zip(df2['Station_Lat'].values, df3['Lat'].values))




import numpy as np

def cartesian_product_simplified(left, right):
    la, lb = len(left), len(right)
    ia2, ib2 = np.broadcast_arrays(*np.ogrid[:la,:lb])

    return pd.DataFrame(
        np.column_stack([left.values[ia2.ravel()], right.values[ib2.ravel()]]))







