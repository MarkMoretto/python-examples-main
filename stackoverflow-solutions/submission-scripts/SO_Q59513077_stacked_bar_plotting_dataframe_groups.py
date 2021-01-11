
"""
Purpose: Stackoverflow: Plotting stacked bar chart
Date created: 2019-12-28

URI: https://stackoverflow.com/questions/59513077/stacked-bar-plotting-dataframe-groups/59513363#59513363

Contributor(s):
    Mark M.
"""


import pandas as pd


dates = ['2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23',
         '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23',
         '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23',
         '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23',
         '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-23',
         '2019-12-23', '2019-12-23', '2019-12-23', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16',
         '2019-12-16', '2019-12-16', '2019-12-16', '2019-12-16']

sources = [
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'passengerterminaltoday.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'airport-suppliers.com',
'passengerterminaltoday.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'airport-suppliers.com',
'passengerterminaltoday.com',
'airport-suppliers.com',
'airport-suppliers.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airport-suppliers.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'airportsinternational.keypublishing.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'passengerterminaltoday.com',
'airport-suppliers.com',
'airport-suppliers.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com',
'internationalairportreview.com'
]


df = pd.DataFrame({"date": dates, "news_source": sources})
# df1['_id'] = [rand_string(35) for i in range(len(df1.index))]

df1 = df.groupby(['date', 'news_source']).size().reset_index().rename(columns={0:'count'})

# Plot results
pd.crosstab(index=df2['date'], columns=df2['news_source'], values=df2['count'], aggfunc=sum)

