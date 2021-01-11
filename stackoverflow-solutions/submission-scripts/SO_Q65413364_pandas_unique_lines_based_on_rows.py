
"""
Purpose: 
Date created: 2020-12-22
https://stackoverflow.com/questions/65413364/how-unique-is-each-row-based-on-3-4-columns
Contributor(s):
    Mark M.
"""

import pandas as pd

cols = ["1", "2", "3"]
rows = [
        ["A", 200, "B",],
        ["A", 200, "B",],
        ["A", 100, "B",],
        ]

df1 = pd.DataFrame(rows, columns=cols)

# Get focus column values before adding a new column.
key_columns = df1.columns.values.tolist()

# Add a line column
df1["line"] = 1

# Set new column to cumulative sum of line values.
df1["match_count"] = df1.groupby(key_columns )['line'].apply(lambda x: x.cumsum())

# Drop line column.
df1.drop("line", axis=1, inplace=True)



print(df1)

