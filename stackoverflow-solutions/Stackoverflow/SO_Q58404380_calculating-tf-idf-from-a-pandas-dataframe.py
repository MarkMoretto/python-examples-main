
"""
Purpose: SO question about max index for multilevel dataframe
Date created: 2019-10-15

Ref: https://stackoverflow.com/questions/58404380/calculating-tf-idf-from-a-pandas-dataframe-without-sklearn/58404464#58404464

Contributor(s):
    Mark M.
"""



import pandas as pd
index = ['11-0.txt','1342-0.txt','1661-0.txt','1952-0.txt','84-0.txt','pg16328.txt',]
cols = ['accept','acceptance','accepted','accepting','access','accessed']

df = pd.DataFrame(index=index, columns=cols)

for i in index:
    for j in cols:
        print(f'df.loc[\'{i}\', \'{j}\'] = ')

df.loc['11-0.txt', 'accept'] = 0.000034
df.loc['11-0.txt', 'acceptance'] = 0.000034
df.loc['11-0.txt', 'accepted'] = 0.000067
df.loc['11-0.txt', 'accepting'] = 0.000034
df.loc['11-0.txt', 'access'] = 0.000336
df.loc['11-0.txt', 'accessed'] = 0.000034
df.loc['1342-0.txt', 'accept'] = 0.000051
df.loc['1342-0.txt', 'acceptance'] = 0.000013
df.loc['1342-0.txt', 'accepted'] = 0.000026
df.loc['1342-0.txt', 'accepting'] = 0.000013
df.loc['1342-0.txt', 'access'] = 0.000153
df.loc['1342-0.txt', 'accessed'] = 0.000013
df.loc['1661-0.txt', 'accept']= 0.000144
df.loc['1661-0.txt', 'acceptance'] = 0.000032
df.loc['1661-0.txt', 'accepted'] =0.000144
df.loc['1661-0.txt', 'accepting'] = 0.000040
df.loc['1661-0.txt', 'access'] = 0.000080
df.loc['1661-0.txt', 'accessed'] = 0.000008
df.loc['1952-0.txt', 'accept'] = 0.000046
df.loc['1952-0.txt', 'acceptance'] = 0.000009
df.loc['1952-0.txt', 'accepted'] = 0.000037
df.loc['1952-0.txt', 'accepting'] = 0.000009
df.loc['1952-0.txt', 'access'] = 0.000092
df.loc['1952-0.txt', 'accessed'] = 0.000009
df.loc['84-0.txt', 'accept'] = 0.000109
df.loc['84-0.txt', 'accepted'] = 0.000218
df.loc['84-0.txt', 'accepting'] =0.000109
df.loc['84-0.txt', 'access'] = 0.001089
df.loc['84-0.txt', 'accessed'] = 0.000109
df.loc['pg16328.txt', 'accept'] = 0.000045
df.loc['pg16328.txt', 'accepted'] = 0.000361
df.loc['pg16328.txt', 'accepting'] =0.000090
df.loc['pg16328.txt', 'access'] = 0.000293
df.loc['pg16328.txt', 'accessed'] = 0.000023



tf_idf = lambda x, y: term-frequency(term) x idf(term)
df1 = df.unstack()

word = 'access'

df[df['access'] == df['access'].max()].index[0]


choice = lambda term, documents: documents[documents[term] == documents[term].max()].index[0]

choice('accept', documents=df)

