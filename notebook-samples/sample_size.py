
"""
Purpose: Sample size
Date created: 2020-11-19

Ref:
    https://www.qualtrics.com/experience-management/research/determine-sample-size/
    https://github.com/shawnohare/samplesize/blob/master/samplesize.py

Contributor(s):
    Mark M.
"""

try:
    from secrets import SystemRandom
except ModuleNotFoundError:
    from random import SystemRandom

from math import exp, inf, pi, sqrt, erf
from statistics import mean, stdev

rnd = SystemRandom()



# import numpy as np
# x = np.linspace(-4, 4, num = 100)
# def get_z_scr_attrs(a = 0.05, n_trials = 100, samples_per_trial = 1000):


# --- Calc. Probability Density Function (PDF) for standard normal distribution --- #
def linspace_(minval, maxval, n_steps = None, stepsize = None):

    minval *= 1.
    maxval *= 1.
    if not n_steps is None:
        n_steps -= 1
        stepsize = float(maxval - minval) / float(n_steps)
    elif not stepsize is None:
        n = float(maxval - minval) / float(stepsize)

    output = list()
    while minval <= maxval:
        output.append(minval)
        minval += stepsize

    return output

lsp = linspace_(-4, 4, maxval = 100)
lsp = linspace_(0., 3.5, stepsize=0.1)


def norm_probability_density(x):
    # lhs_constant = 1. / sqrt(2 * pi)
    def phi(x):
        'Cumulative distribution function for the standard normal distribution'
        return (1.0 + erf(x / sqrt(2.0))) / 2.0
    value = 0.
    for i in range(-inf, x):
        value += phi()

idx_range = list(map(lambda x: round(x/10, 2), range(0, 36)))
col_range = list(map(lambda x: round(x/100, 2), range(0, 11)))
matrix = [[0.] * len(idx_range) for _ in range(len(col_range))]
for r in range(len(idx_range)):
    for c in range(len(col_range)):
        matrix[c][r] = round(idx_range[r] + col_range[c], 4)



constant = 1 / sqrt(2 * pi)
alpha = 0.05
conf_level = 1 - alpha

n_trials = 1000
epochs  = 100

results = []
for n in range(epochs):
    # rand_vals = [rnd.uniform(0, 1) for _ in range(n_trials)]
    rand_vals = [rnd.random() for _ in range(n_trials)]
    results.append(sum([1 if i <= conf_level else 0 for i in rand_vals]) / n_trials)
mean(results)



def cls_prop(name, datatype):
    """Class property helper function."""

    mask_name = f"__{name}"

    @property
    def this_prop(self):
        return getattr(self, mask_name)

    @this_prop.setter
    def this_prop(self, value):
        if not isinstance(value, datatype):
            raise TypeError(f"Expected data type {datatype}!")
        setattr(self, mask_name, value)

    return this_prop

class SampleSize:
    cls_prop("population_size", str)
    cls_prop("alpha", float)
    cls_prop("margin_of_error", float)
    def __init__(self, population_size, alpha=0.05, margin_of_error = 0.05):
        self.population_size = population_size
        self.alpha = alpha
        self.ci = 1 - alpha
        self.margin_of_error = margin_of_error











# Calculated

import scipy.stats as ss

def _get_conf_lvl(a):
    return round(ss.norm.ppf(1 - (a/2)), 4)

def sampleSize(population_size, margin_error = .05, confidence_level = .99, sigma = 1/2):
    """
    Calculate the minimal sample size to use to achieve a certain
    margin of error and confidence level for a sample estimate
    of the population mean.
    Inputs
    -------
    population_size: integer
        Total size of the population that the sample is to be drawn from.
    margin_error: number
        Maximum expected difference between the true population parameter,
        such as the mean, and the sample estimate.
    confidence_level: number in the interval (0, 1)
        If we were to draw a large number of equal-size samples
        from the population, the true population parameter
        should lie within this percentage
        of the intervals (sample_parameter - e, sample_parameter + e)
        where e is the margin_error.
    sigma: number
        The standard deviation of the population.  For the case
        of estimating a parameter in the interval [0, 1], sigma=1/2
        should be sufficient.
    """
    alpha = 1 - (confidence_level)
    zdict = {
        .90: 1.645,
        .91: 1.695,
        .99: 2.576,
        .97: 2.17,
        .94: 1.881,
        .93: 1.812,
        .95: 1.96,
        .98: 2.326,
        .96: 2.054,
        .92: 1.751
    }
    if confidence_level in zdict:
        z = zdict[confidence_level]
    else:
        from scipy.stats import norm
        z = norm.ppf(1 - (alpha/2))

    z = _get_conf_lvl(alpha)

    N = population_size
    M = margin_error
    numerator = z**2 * sigma**2 * (N / (N-1))
    denom = M**2 + ((z**2 * sigma**2)/(N-1))
    return numerator/denom


n = 768
moe = 0.05
alpha = 0.01
std = 0.5
z = _get_conf_lvl(alpha)

const = z**2 * std**2

numerator = const * (n / (n-1))
denom = (moe ** 2) + (const / (n-1))

samplesize = (numerator//denom)+1