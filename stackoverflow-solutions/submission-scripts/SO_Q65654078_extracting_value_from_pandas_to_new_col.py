
"""
Purpose: Stackoverflow solution
Date created: 2021-01-10

URL: https://stackoverflow.com/questions/65654078/why-am-i-gettting-all-nan-while-appending-a-new-field-to-a-data-frame/65654163#65654163

Contributor(s):
    Mark M.
"""


import pandas as pd

ddict = dict(file=[
    "FFIEC CDR Call Schedule RCB02 03312011.txt",
    "FFIEC CDR Call Schedule RCB02 03312011.txt",
    "FFIEC CDR Call Schedule RCB02 03312011.txt",
    "FFIEC CDR Call Schedule RCB02 03312011.txt",
    "FFIEC CDR Call Schedule RCB02 03312011.txt",
    "FFIEC CDR Call Schedule RCB03 03312011.txt",
])

df = pd.DataFrame(ddict)


df.loc[:, "schedule_code"] = df["file"].str.extract(r"FFIEC CDR Call Schedule (\w+) \d+\.txt").values

