import numpy as np 
from sklearn.cluster import SpectralClustering
from sklearn import datasets
wine = datasets.load_wine()
spc= SpectralClustering(n_clusters=3,
affinity='nearest_neighbors')
spc.fit(wine.data)
# 結果の評価
from sklearn.metrics.cluster import normalized_mutual_info_score
eval = normalized_mutual_info_score(spc.labels_, wine.target)
print(eval)