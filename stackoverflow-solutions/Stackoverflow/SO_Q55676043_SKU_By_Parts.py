


"""
Ref: https://stackoverflow.com/questions/55676043/building-a-feed-by-manipulating-data-from-another-feed-using-python-pandas#55676043
"""

import pandas as pd

pd.options.mode.chained_assignment = None

catprod = {'1513':'combinezonb', '2755':'jeansdama','2513':'combinezondama'} # code for each product type
jeansdama = {'24':'002', '25':'003', '26':'003'} # this are code sizes for jeans
combinezondama = {'21':'002','23':'002','24':'003'} # this are code sizes from women leather suits

"""
So each product type has different sizes # code sizes. 

#After I solve the SKU problems I have to check ITEM CODE row by row and add a new row when similar product is found.

What have I done so far:

 1. Created the dictionaries for product types and dictionary for product type sizes
 2. Imported the test feed and managed to export it to a suitable structure
 3. Started iterating the dataframe row by row and searching if ITEM CODE contains the product category code ('2755') and based on the size tried to set a code size variable.

"""

ddict = {
    'ITEM CODE':['1513452', '1513458', '1513463', '2513452', '1533790', '1553707', '1614054', '2755126', '2755126', '2755134', '2755134'],
    'COLOR CODE':['685','948','22A','685','691','948','631','Y17','Y18','348','T46'],
    'TG':['24', '24', '24', '21', '24', '24', '24', '24', '24', '24', '24'],
    }

df3 = pd.DataFrame(ddict)
df3['tomatch'] = [i[:4] for i in df3['ITEM CODE']]
df3['combokey'] = df3['TG'] + df3['tomatch']
df3 = df3.drop(['tomatch','TG',], axis=1)


catprod = {"2755":"jeansdama",
           "2513":"combinezondama",
           "2D10":"combinezondama",
           "1755":"jeansbarbat",
           "1513":"combinezonbarbat",
           "1D10":"combinezonbarbat"}

cp_dict = {
    'CODE': [i for i in catprod.keys()],
    'desc':[i for i in catprod.values()],
    }
cp_df = pd.DataFrame(cp_dict)



jeansdama = {"24": "002",
             "25": "003",
             "26": "004",
             "27": "005",
             "28": "006",
             "29": "007",
             "30": "008",
             "31": "009",
             "32": "010",
             "33": "011",
             "34": "012",
             "35": "013",
             "36": "014"}

jd_dict = {
    'TG': [i for i in jeansdama.keys()],
    'jd_size':[i for i in jeansdama.values()],
    }

jd_df = pd.DataFrame(jd_dict)
jd_df['name'] = 'jeansdama'

df2 = cp_df.merge(jd_df, how ='outer', left_on='desc', right_on='name')
df2 = df2.drop('name', axis=1).copy()
df2= df2[df2['TG'].isna() == False]
df2['combokey'] = df2['TG'] + df2['CODE']
df2 = df2.drop('TG', axis=1)
df_main = df3.join(df2.set_index('combokey'), on='combokey')

# df_main = df3.merge(df2, how ='outer', left_on=['tomatch','TG'], right_on=['CODE','TG'])
try:
    df_main.drop('CODE',axis=1, inplace=True)
except KeyError:
    pass


combinezondama = {"38": "002",
                  "40": "003",
                  "42": "004",
                  "44": "005",
                  "46": "006",
                  "48": "007",
                  "50": "008",
                  "52": "009",
                  "54": "010"}

cz_dict = {
    'TG': [i for i in combinezondama.keys()],
    'cz_size':[i for i in combinezondama.values()],
    }
cz_df = pd.DataFrame(cz_dict)
cz_df['name'] = 'combinezondama'
df2 = cp_df.merge(cz_df, how ='outer', left_on='desc', right_on='name')
df2 = df2.drop('name', axis=1).copy()
df2= df2[df2['TG'].isna() == False]
df2['combokey'] = df2['TG'] + df2['CODE']
df2 = df2.drop('TG', axis=1)
df_main = df_main.join(df2.set_index('combokey'), on='combokey')



df2 = cp_df.merge(cz_df, how ='outer', left_on='desc', right_on='name')
df2.drop('name', axis=1, inplace=True)
df2= df2[df2['TG'].isna() == False]
df_main = df_main.merge(df2, how ='outer', left_on=['tomatch','TG'], right_on=['CODE','TG'])

df_main = df3.merge(df2, how ='outer', left_on=['tomatch','TG'], right_on=['CODE','TG'])

try:
    df_main.drop('TG_y',axis=1, inplace=True)
except KeyError:
    pass







df3['desc'] = [catprod[k] for k in catprod.keys() for i in df3['tomatch']]

for i in df3['ITEM CODE']:
    for k in catprod.keys():
        if i.startswith(k):
            df3['desc'] = catprod[k]

for i, row in df3.iterrows():
    if '2755' in df3['ITEM CODE'][i] and '24' in df3['TG'][i]:
            codmarime = '002'
            print(codmarime)
            df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+codmarime
            print(df3['SKU'][i])
            codmarime = ''
    elif '2755' in df3['ITEM CODE'][i] and '25' in df3['TG'][i]:
        codmarime = '003'
        df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+codmarime
        codmarime = ''
    elif '2755' in df3['ITEM CODE'][i] and '26' in df3['TG'][i]:
        codmarime = '004'
        df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+codmarime
        codmarime = ''
    #2513 combinezon dama
    elif '2513' in df3['ITEM CODE'][i] and '21' in df3['TG'][i]:
        codmarime = '???'
        df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+codmarime
        codmarime = ''
    # N = marimi universale 001 cod
    elif df3['TG'][i] == 'N':
        codmarime = '001'
        df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+codmarime
        codmarime = ''
    else:
        df3['SKU'][i] = '20'+df3['ITEM CODE'][i]+df3['COLOR CODE'][i]+'???'
        codmarime = ''
    print(df3['SKU'])
    df3['name'] = 'DAINESE'+' '+df3['ITEM']+' '+df3['COLOR']+' MARIMEA '+df3['TG']
    codmarime = ''