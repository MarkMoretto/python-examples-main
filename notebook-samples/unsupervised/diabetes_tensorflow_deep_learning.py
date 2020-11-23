
"""
Purpose: Binary classificaton for diabetes patients.
Date created: 2020-11-06

Ref: https://github.com/tirthajyoti/Deep-learning-with-Python/blob/master/Notebooks/Keras_Scikit_Learn_wrapper.ipynb

Contributor(s):
    Mark M.
"""

import warnings
warnings.filterwarnings('ignore')

import os
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import scipy.stats as ss

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import minmax_scale

from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import (
        cross_val_score,
        GridSearchCV,
        StratifiedKFold,
        )

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

mpl.rcParams['figure.dpi'] = 150


pd.set_option("mode.chained_assignment", None)
pd.set_option("display.width", 120)
pd.set_option("display.date_yearfirst", True)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_info_rows", 10000)


LOCAL_DEV = True

# Set local folder if developing/debugging
if LOCAL_DEV:
    myuser = os.environ["username"]
    PROJECT_FOLDER = Path(rf"C:\Users\{myuser}\Desktop\Info\GitHub\python-examples-main\notebook-samples\unsupervised")
    os.chdir(PROJECT_FOLDER)

csv_url = "https://raw.githubusercontent.com/tirthajyoti/Deep-learning-with-Python/master/Data/pima-indian-diabetes.csv"
csv_path = PROJECT_FOLDER.joinpath(r"data\pima-indian-diabetes.csv")


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

    z = _get_conf_lvl(alpha)

    N = population_size
    M = margin_error
    numerator = z**2 * sigma**2 * (N / (N-1))
    denom = M**2 + ((z**2 * sigma**2)/(N-1))
    return numerator/denom



# 10-fold cross-validation

# params = dict(
#         loss = "binary_crossentropy",
#         optimizer = "adam",
#         metrics = ["accuracy"],
#         )

def keras_10_cv_model():
    model = Sequential()
    model.add(Dense(30, input_dim=8, activation = 'relu'))
    model.add(Dense(15, activation = 'relu'))
    model.add(Dense(1, activation = 'relu'))

    # Compile and output
    model.compile(loss = "binary_crossentropy",
                  optimizer = "adam",
                  metrics = ["accuracy"],
                  )
    return model


data = np.loadtxt(csv_path, delimiter=",", skiprows=1)
df = pd.read_csv(csv_url, sep=",", low_memory=False)

"""
Memory reduction
"""
mb_from_kb = lambda size_in_bytes, kb = 2**10: size_in_bytes / kb ** 2
pre_downsize = mb_from_kb(df.memory_usage().sum())

for c in df.select_dtypes(include=["int64"], exclude=["object"]).columns:
    df.loc[:, c] = pd.to_numeric(df.loc[:, c], downcast="integer")

post_downsize = mb_from_kb(df.memory_usage().sum())
print(f"Pre-downsize mem usage: {pre_downsize:.4f}\nPost-downsize mem usage: {post_downsize:.4f}")


dependent_variable = "Outcome"

def print_dependent_var_metrics(var):
    df_desc = df.describe()

    dep_mu = df_desc.loc["mean", var]
    dep_sigma = df_desc.loc["std", var]
    print(f"\nDependent variable '{var}' has:\n\tMean: {dep_mu:.4f}\n\tStd. dev.: {dep_sigma:.4f}")

# print_dependent_var_metrics(dependent_variable)

# Split into input and output variables
# X = data[:, :8]
# y = data[:, 8]

X = df.drop(dependent_variable, axis=1)
y = df.loc[:, dependent_variable]


X_scaled = minmax_scale(X.values)


N_FOLDS = 10


# --- Main Keras model --- #
kc_model = KerasClassifier(build_fn = keras_10_cv_model,
                        epochs = 10,
                        batch_size = 32,
                        verbose = 0,
                        )


kc_kfold = StratifiedKFold(n_splits = N_FOLDS, shuffle=True)


cv_results = cross_val_score(kc_model, X_scaled, y, cv = kc_kfold, verbose = 2,)



# Mean and standard deviation results
print(f"CV Mean: {cv_results.mean():.4f}")
print(f"CV Std. Dev: {cv_results.std():.4f}")




# --- Exhaustive Grid Search --- #

def create_model_grid(activation = 'relu', 
                      optimizer='rmsprop',
                      init='glorot_uniform'):
    # create model
    model = Sequential()
    
    if activation=='relu':
        model.add(Dense(12, input_dim=8,
                        kernel_initializer=init, activation='relu'))
        model.add(Dense(8, kernel_initializer=init, activation='relu'))
    if activation=='tanh':
        model.add(Dense(12, input_dim=8, 
                        kernel_initializer=init, activation='tanh'))
        model.add(Dense(8, kernel_initializer=init, activation='tanh'))
    if activation=='sigmoid':
        model.add(Dense(12, input_dim=8, 
                        kernel_initializer=init, activation='sigmoid'))
        model.add(Dense(8, kernel_initializer=init, activation='sigmoid'))
    model.add(Dense(1, kernel_initializer=init, activation='sigmoid'))
    
    # Compile model
    model.compile(loss='binary_crossentropy', 
                  optimizer=optimizer, 
                  metrics=['accuracy'])
    return model



model_grid = KerasClassifier(build_fn=create_model_grid, verbose=0)


activations = ['tanh','relu','sigmoid']
optimizers = ['rmsprop', 'adam','sgd']
initializers = ['glorot_uniform', 'normal', 'uniform']
epochs = [5,10,25]
batches = [8,16,64]
















