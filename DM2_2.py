import pandas as pd
import numpy as np
import scipy.stats
import heapq
from sklearn.linear_model import LinearRegression
data = pd.read_csv("winequality-red.csv", sep=";")
data2 = data.values
xdata = data2[:,:11]
ydata = data2[:,11]
xdata2 = scipy.stats.zscore(xdata)


model = LinearRegression()
model.fit(xdata２, ydata)

coefficients = model.coef_

#print(coefficients)

indices = heapq.nlargest(3, range(len(coefficients)), key = lambda x: coefficients[x])

print("上位3属性のインデックス")
print(indices)