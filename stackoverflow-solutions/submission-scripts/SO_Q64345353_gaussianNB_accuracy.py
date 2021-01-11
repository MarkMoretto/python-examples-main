
"""
Purpose: 
Date created: 2020-10-13

https://stackoverflow.com/questions/64344902/getting-errors-when-trying-to-calculate-accuracy-on-gaussiannb/64345353#64345353


Contributor(s):
    Mark M.
"""


from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

data = fetch_california_housing()
c = np.array([1 if y > np.median(data['target']) else 0 for y in data['target']])
X_train, X_test, c_train, c_test = train_test_split(data['data'], c, random_state=0)

gaussian=GaussianNB().fit(X_train, c_train)
pred=gaussian.predict(X_test)

X_test.shape[0]
(c_test != pred).sum() / X_test.shape[0]

result = accuracy_score(c_test, pred)
1 - ((c_test != pred).sum() / X_test.shape[0])

