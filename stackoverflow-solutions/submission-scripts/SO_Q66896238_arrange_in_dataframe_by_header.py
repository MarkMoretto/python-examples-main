
"""
https://stackoverflow.com/questions/66896238/how-to-arrange-data-in-dataframes-according-to-headers-python/66896461?noredirect=1#comment118252081_66896461

"""
import pandas as pd



ddict = {
"column1": ["Name=John","Name=Roy","Name=Smith","Age=12","Name=jason","Age=1",],
"column2": ["Age=25","Age=36","Age=19","Name=Donald","Age=57","Name=joe",]
}


df = pd.DataFrame(ddict)


coldict = dict.fromkeys(df.columns.values.tolist(), None)
for c in coldict.keys():
    coldict[c] = df[c].str.split("=", expand=True)[0].value_counts().to_dict()

for col, d in coldict.items():
    [k for k, v in d.items() if v == max(d.values())]


df[df.columns[0]].str.split("=", expand=True)[0].value_counts()

# Create a copy of the dataframe
df2 = df.copy()

# Look in the Age field where the right-side is non-numeric;
# Set that value to name
df.loc[df2["Age"].str.match(r"^\w+=\D+$"), "Name"] = df2.loc[df2["Age"].str.match(r"^\w+=\D+$"), "Age"]

# Do the opposite for the other field.
df.loc[df2["Name"].str.match(r"^\w+=\d+$"), "Age"] = df2.loc[df2["Name"].str.match(r"^\w+=\d+$"), "Name"]