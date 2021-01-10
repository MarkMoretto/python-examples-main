

"""
Scenario:
    Evaluate values in two dataframe columns.
    If one column larger than the other, populate third column with geometric mean
    of the value in a given column from the current row and one prior.

Date create: 2019-03-16
Contributor: Mark Moretto

Ref: https://stackoverflow.com/questions/55196029/calculate-difference-for-specific-rows#55196074
"""

import pandas as pd
from functools import reduce

__name__ = 'RunScript'

ddict = {
    'Date':['1999-07-21','1999-07-22','1999-07-23','1999-07-24',],
    'price':[8.6912,8.6978,8.8127,8.8779],
    'mid':[8.504580,8.508515,8.524605,8.688810],
    'std':[0.084923,0.092034,0.118186,0.091124],
    'top':[9.674425,8.692583,10.760976,8.871057],
    'btm':[8.334735,8.324447,8.288234,8.506563],
    }


data = pd.DataFrame(ddict)


def geo_mean(iter):
    """
        Geometric mean function. Pass iterable
    """
    return reduce(lambda a, b: a * b, iter) ** (1.0 / len(iter))


def set_geo_mean(df):
    # Shift the price row down one period
    data['shifted price'] = data['price'].shift(periods=1)

    # Create a masked expression that evaluates price vs top
    masked_expression = df['price'] > df['top']

    # Return rows from dataframe where masked expression is true
    masked_data = df[masked_expression]

    # Apply our function to the relevant rows
    df.loc[masked_expression, 'geo_mean'] = geo_mean([masked_data['price'], masked_data['shifted price']])

    # Drop the shifted price data column once complete
    df.drop('shifted price', axis=1, inplace=True)


if __name__ == 'RunScript':
    # Call function and pass dataframe argument.
    set_geo_mean(data)