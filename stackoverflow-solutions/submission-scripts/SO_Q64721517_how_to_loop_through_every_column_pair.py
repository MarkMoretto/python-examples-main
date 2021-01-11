
"""O
Purpose: 
Date created: 2020-11-06

https://stackoverflow.com/questions/64721517/how-to-loop-through-every-column-pair

Contributor(s):
    Mark M.


Desc:
    I have an excel file that is 199 x 15 (has 15 columns and 199 rows). My job is to 
    compute the stats for every pairs of 15 columns. Basically column (1,2), (1,3), 
    (1,4), ... (14,15)... and so on for all pairs.I have to do it for each of the 105 
    (15×14/2) pairs of variables provided. The stats I want to calculate is the chi 
    square . Here is what I have so far:    
"""


import itertools
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, chi2
from scipy.stats import ttest_ind
# from bioinfokit.analys import stat, get_data, chisq
from itertools import combinations

df = pd.read_csv(r'C:\Users\ether\OneDrive\Desktop\info.csv')

deg_of_frdm = 15
data = np.random.randint(0, 5, (199, 15))
p_value_matrix = np.zeros((15, 15))

mean, var, skew, kurt = chi2.stats(deg_of_frdm, moments='mvsk')
sigma = np.sqrt(var)
# x = np.linspace(chi2.ppf(0.01, deg_of_frdm), chi2.ppf(0.99, deg_of_frdm), 199)

chi2.cdf(np.array((data[:, 0][:, None], data[:, 1][:, None])), mean, sigma)
p_val = chi2.cdf(np.array((data[:, 0], data[:, 1])), mean, sigma)
p_val = chi2.cdf(np.array((data[:, 0][:, None], data[:, 1][:, None])).mean(), mean, sigma)


i_mean = np.mean(data[:, 0])
j_mean = np.mean(data[:, 1])
i_std = np.std(data[:, 0])
j_std = np.std(data[:, 1])
ttest, pval = ttest_ind(data[:, 0], data[:, 1])


chi_sq_func = lambda o_vals, e_vals: sum([(o - e)**2. / e for o, e in zip(o_vals, e_vals)])


contingency_table = pd.crosstab(data[:, 0], data[:, 1])
observed_values = contingency_table.values
b = chi2_contingency(contingency_table)
n_cols = len(contingency_table.columns)
n_rows = len(contingency_table.index)
ddof = (n_rows-1) * (n_cols-1)

alpha = 0.05

expected_values = b[3]
chi_squares = sum([(obs-expct)**2. / expct for obs, expct in zip(observed_values, expected_values)])
chi_square_statistic = chi_squares[0] + chi_squares[1]

critical_value = chi2.ppf(q = 1 - alpha, df = ddof)


p_value = 1 - chi2.cdf(x = chi_square_statistic, df = ddof)



if chi_square_statistic > =critical_value:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")


if p_value <= alpha:
    print("Reject H0,There is a relationship between 2 categorical variables")
else:
    print("Retain H0,There is no relationship between 2 categorical variables")



data = np.random.randint(0, 5, (199, 15))
p_value_matrix = np.zeros((15, 15))

chi_sq_func = lambda o_vals, e_vals: sum([(o - e)**2. / e for o, e in zip(o_vals, e_vals)])

alpha = 0.05

# Based on 5 X 5 contingency table.
n_cols, n_rows, ddof = 5, 5, 16


for i, j in combinations(range(15), 2):

    contingency_table = pd.crosstab(data[:, i], data[:, j])

    observed_values = contingency_table.values

    b = chi2_contingency(contingency_table)

    expected_values = b[3]

    chi_squares = chi_sq_func(observed_values, expected_values)
    chi_square_statistic = chi_squares[0] + chi_squares[1]
    
    critical_value = chi2.ppf(q = 1 - alpha, df = ddof)

    p_val = 1 - chi2.cdf(x = chi_square_statistic, df = ddof)

    p_value_matrix[i, j] = p_value_matrix[j, i] = p_val
    if p_val < alpha:
        print('possibly dependent: {} -- {}'.format(i, j))





    # n_cols = len(contingency_table.columns)
    # n_rows = len(contingency_table.index)

    # ddof = (n_rows-1) * (n_cols-1)
    # print(f"processing pairs: ({i}, {j})\nN rows: {n_rows}, n cols: {n_cols}, ddof: {ddof}")