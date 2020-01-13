
"""
BIC algoritm for KMeans and other relevant models
"""

__all__ = ['compute_bic',]

import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import squareform

### Implement example through several KMeans iterations
# BIC = [compute_bic(kmeansi, X) for kmeansi in KMeans]

def slice_by_axis(arr, indices, axis):
    sl = [slice(None)] * arr.ndim
    sl[axis] = indices
    return arr[sl]

def compute_bic(cluster_model, X):

    ### Get centers, labels, and cluster number from model
    centers = cluster_model.cluster_centers_
    labels  = cluster_model.labels_
    m = cluster_model.n_clusters

    ### Value count for each label
    n = np.bincount(labels)

    ### N = numer of observations, d = number of dimensions
    N, d = X.shape

    ### Computing cluster variance; Some data needed to be reworked and shaped
    cluster_var = (1.0 / (N - m) / d) * sum([sum(distance.cdist(X[np.where(labels == i)].reshape(-1, 1), slice_by_axis(centers, i, 0).reshape(-1, 1), 'euclidean')**2) for i in range(m)])

    ### Calculate 
    const = 0.5 * m * np.log(N) * (d + 1)

    ### Compute BIC with calculated inputs
    BIC = np.sum(
        [n[i] * np.log(n[i]) 
         - n[i] * np.log(N) 
         - ((n[i] * d) / 2) * np.log(2 * np.pi * cluster_var) 
         - ((n[i] - 1) * d / 2) for i in range(m)]
        ) - const

    ### Multiply by -1 to account for inverse result
    return(BIC * -1)
