
"""
Purpose: Stackv
Date created: 2021-01-09

https://stackoverflow.com/questions/65642266/finding-maxima-and-minima-at-certain-points-pandas-python/65644462#65644462

Contributor(s):
    Mark M.
"""

from itertools import combinations, product
import pandas as pd
import numpy as np

toy = pd.DataFrame({
                'price': [100, 103, 107, 105, 99, 96, 98, 103],
                'barrier': [102, 102, 102,102,102,102, 102, 102],
                'date': ['2020-02-28', '2020-03-01', '2020-03-02','2020-03-03', '2020-03-04', '2020-03-05', '2020-03-06', '2020-03-07']})


toy['date'] = pd.to_datetime(toy['date']) #just make datetime obj
toy['rets'] = np.log(toy['price']/toy['price'].shift(1))
toy['ret_cum'] = toy['rets'].cumsum()
toy['loop'] = [0, 103, 0, 0, 99, 0, 0, 103] #some signal
toy['inten'] = 0.0 #initialize



start = -1
stop = -1
count = 0
for i in toy.index:
    if stop > max(toy.index):
        break
    if toy.loc[i, "loop"] != 0:
        if count == 0:
            start = i
        else:
            stop = i
            if count % 2 == 0:
                toy.loc[i, "inten"] = toy.loc[start:stop, "ret_cum"].min()
            else:
                toy.loc[i, "inten"] = toy.loc[start:stop, "ret_cum"].max()
            start = stop + 1
        count += 1



