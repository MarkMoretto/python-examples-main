
"""
Purpose: Decision Trees / Random Forests
Date created: 2020-06-08

Ref: https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.08-Random-Forests.ipynb
Interactive: https://github.com/jakevdp/PythonDataScienceHandbook/blob/8a34a4f653bdbdc01415a94dc20d4e9b97438965/notebooks/06.00-Figure-Code.ipynb

Contributor(s):
    Mark M.
"""


import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier

SAMPLE_SIZE=300
N_CENTERS=4

X, y = make_blobs(n_samples=SAMPLE_SIZE, centers=N_CENTERS, random_state=13)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap="rainbow")


dtree = DecisionTreeClassifier().fit(X, y)

