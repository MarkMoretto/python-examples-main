
# https://stackoverflow.com/questions/55313848/for-every-pandas-dataframe-made-count-the-number-of-values-satisfying-a-conditi

import pandas as pd

ddict = {
    'Date':['2016-01-01','2016-01-01','2016-01-01','2016-01-01','2016-01-01','2016-01-02',],
    'Hour':['00','01','02','03','04','02'],
    'Location':['Street','Street','Street','Street','Street','Street',],
    'N02_Level':[19,39,129,76,40, 151],
}

df = pd.DataFrame(ddict)

# Convert dates to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Make a Year column
df['Year'] = df['Date'].apply(lambda x: x.strftime('%Y'))

# Group by lcoation and year, count by M02_Level > 150
df1 = df[df['N02_Level'] > 150].groupby(['Location','Year']).size().reset_index(name='Count')

# Interate the results
for i in range(len(df1)):
    loc = df1['Location'][i]
    yr = df1['Year'][i]
    cnt = df1['Count'][i]
    print(f'{loc},{yr},{cnt}')


### To not use f-strings
for i in range(len(df1)):
    print('{loc},{yr},{cnt}'.format(loc=df1['Location'][i], yr=df1['Year'][i], cnt=df1['Count'][i]))