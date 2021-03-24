
"""
Purpose: Stackoveflow
Date created: 2021-02-28

Title: extract data from website pandas read_html
URL: https://stackoverflow.com/questions/66415389/extract-data-from-website-pandas-read-html/66415557#66415557

Contributor(s):
    Mark M.
"""


import pandas as pd

url = "https://www.sqimway.com/lte_band.php"


lte_band = pd.read_html(url)

# Set a new DataFrame variable.
df = lte_band[0]


# Requires pandas 0.24+
df.columns = list(map(lambda q: " ".join(sorted(set(q), key = q.index)), df.columns.to_flat_index()))




######################
# --- Other Work --- #
######################

# Create an empty list
new_cols = []
df.columns.to_flat_index().map(" ".join(set))

for c in df.columns:
    # Check equaltiy and take one value if True
    if c[0] == c[1] == c[2]:
        new_cols.append(c[0])
    else:
        # Join the rest of the column values.
        new_cols.append(" ".join(set([c[i] for i in range(3)])))

# Concatenate current columns
df.columns = df.columns.map(" ".join)
col_map = dict(zip(list(df.columns), new_cols))

df1 = df.rename(columns = col_map, level=0, inplace = False)
