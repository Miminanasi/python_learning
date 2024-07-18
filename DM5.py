import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
wine = datasets.load_wine()
km = KMeans(n_clusters=3, random_state=10)
km.fit(wine.data)
#ans = km.fit_predict(wine.data)
#eval = normalized_mutual_info_score(ans, wine.target)

from sklearn.metrics.cluster import normalized_mutual_info_score
eval = normalized_mutual_info_score(km.labels_,wine.target)
print(eval)