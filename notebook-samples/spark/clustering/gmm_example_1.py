
"""
Purpose: Gaussian Mixture Model
Date created: 2021-07-16

Dir: C:\\Users\\Work1\\Desktop\\Info\\GitHub\python-examples-main\notebook-samples\spark\clustering

Contributor(s):
    Mark M.
"""

from pathlib import Path
from numpy import array

from pyspark import SparkContext
from pyspark.mllib.clustering import GaussianMixture, GaussianMixtureModel

datadir = Path(r"C:\Users\Work1\AppData\Local\Programs\spark-3.1.2-bin-hadoop2.7\data\mllib")

sample_data_path = datadir.joinpath("gmm_data.txt")

# with gmm_data.open() as f:
#     data = f.read()

if __name__ == "__main__":
    sc = SparkContext(appName="GMMExample")
    
    data = sc.textFile(str(sample_data_path))
    lines = data.map(lambda l: array([float(i) for i in line.strip().split(" ")]))
    
    gmm = GaussianMixture.train(lines, k=2)
    
    # Save and load data
    # gmm_file_path = Path().joinpath(r"data\gmm-model")
    # gmm.save(sc, str(gmm_file_path))
    # gmm_model = GaussianMixtureModel.load(sc, str(gmm_file_path))
    
    
    # Output model params
    for i in range(2):
        print(f"weight = {gmm.weights[i]}, mu = {gmm.gaussians[i].mu}, sigma = {gmm.gaussians[i].sigma.toArray()}")
    
    sc.stop()
