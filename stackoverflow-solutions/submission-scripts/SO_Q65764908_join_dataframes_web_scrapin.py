
"""
Purpose: Stackoveflow solution
Date created: 2021-01-17
URL: https://stackoverflow.com/questions/65764908/how-do-i-join-dataframes-in-python-where-each-dataframe-has-a-column-which-repre/65765147#65765147

Contributor(s):
    Mark M.
"""


import pandas as pd

df = pd.DataFrame({
        "Item": ["Car", "Bike", "Car", "Bike", "Car", "Bike",],
        "Price": ["100", "", "200", "10", "150", "10"],
        })

df["partition"] = df.groupby("Item").cumcount()

pd.merge(df, df, left_on=["Item", "Price"], right_on=["Item", "Price"], sort=False)


result = df.pivot(index="Item", columns="partition", values="Price")

