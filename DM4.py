import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split

import pickle 
with open('covdata.pkl','br') as fr:
    covdata = pickle.load(fr)

x = covdata.data
y = covdata.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
clf = LDA()
clf.fit(x_train,y_train)
sc = clf.score(x_test,y_test)
print(sc)