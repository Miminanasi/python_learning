from sklearn import datasets, decomposition
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data.astype(np.float32)

pca= decomposition.PCA(n_components= 2)
pca.fit(X)
X2=pca.transform(X)

plt.plot(X2[:50,0], X2[:50,1], "o") # setosa
plt.plot(X2[50:100,0], X2[50:100,1], "x") # versicolor
plt.plot(X2[100:,0], X2[100:,1], "+") #virginica
plt.show()