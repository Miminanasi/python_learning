import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn import mixture
from sklearn import datasets
wine = datasets.load_wine()
g = mixture.GaussianMixture(n_components=3,covariance_type='diag')
g.fit(wine.data)
ans= g.predict(wine.data)

eval = normalized_mutual_info_score(ans, wine.target)
print(eval)