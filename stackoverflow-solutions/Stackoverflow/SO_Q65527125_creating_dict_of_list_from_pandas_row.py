
"""
Purpose: Stackoverflow solution.
Date created: 2020-12-31
URL: https://stackoverflow.com/questions/65527125/creating-a-dict-of-list-from-pandas-row/65527238#65527238


Contributor(s):
    Mark M.
"""


import pandas as pd


ddict = {
"Barker Minerals Ltd": ["", "", "", "",],
"Blackout Media Corp": ["", "", "", "",],
"Booking Holdings Inc": ["Booking Holdings Inc","Booking Holdings Inc 4.10 04/13/2025","BOOKING HOLDINGS INC", "",],
"Baker Hughes Company": ["Baker Hughes Company","BAKER HUGHES A GE COMPANY LLC-3.34%-12-15-2027","BAKER HUGHES A GE COMPANY LLC-3.14%-11-7-2029", "",],
"Bank of Queensland Limited": ["Bank of Queensland Limited" ,"Bank of Queensland Limited FRN 10-MAY-2026 3.50% 05/10/26","Bank of Queensland Limited FRN 26-OCT-2020 1.27% 10/26/20", "Bank of Queensland Limited FRN 16-NOV-2021 1.12% 11/16/21"],
}


df = pd.DataFrame.from_dict(ddict, orient='index', columns = range(len(ddict)-1))

result_dict = {k:list(d.values()) for k, d in df.to_dict(orient="index").items()}
