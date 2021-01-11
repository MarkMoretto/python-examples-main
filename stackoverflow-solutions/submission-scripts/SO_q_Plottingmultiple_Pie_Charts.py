
"""
Purpose: 
Date created: 2019-12-22

Contributor(s):
    Mark M.
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
         {'Keys': ['key1','key2','key3'],
          'Percentage':[63,37,89]}
         )


# df['key_yes'] = df['Keys'].values + '_yes'
# df['key_no'] = df['Keys'].values + '_no'


df['yes'] = df['Percentage']/100
df['no'] = 1 - df['yes']

df.index = df['Keys'].values

df.drop(['Keys', 'Percentage'], axis=1, inplace=True)



key_count = len(df.index)
for i,v in enumerate(range(key_count)):
    v = v+1
    ax1 = subplot(key_count, 1, v)
    labels = df.loc[0, 'Keys']
    sizes = [df.loc[0, 'yes'], df.loc[0, 'no']]
    plt.pie(sizes, shadow=True, startangle=90, ax=ax1)
plt.axis('equal')
plt.tight_layout()
plt.show()

for i in len(df.index):
    plt.figure(i)
    labels = df.loc[0, 'Keys']
    sizes = [df.loc[0, 'yes'], df.loc[0, 'no']]
    plt.pie(sizes, shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()
plt.show()

# df.drop(['Keys','Percentage',], axis=1, inplace=True)

plt.figure(figsize=(16,8))
ax1 = plt.subplot(121, aspect='equal')
df.plot(kind='pie', y = 'Percentage', ax=ax1, autopct='%.3f%%',
        startangle=90, shadow=False, labels=df['Keys'], legend = False, fontsize=11)

plt.show()







fig, axs = plt.subplots(2, 2)
for i in df.index:
    df.iloc[i, :].plot(x='Keys', y='Percentage'kind='pie')


df.plot(y='Percentage',kind='pie', subplots=True, figsize=(9, 7))
plt.axis('equal')
plt.show()