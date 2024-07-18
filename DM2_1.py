import pandas as pd
import numpy as np
data = pd.read_csv("winequality-red.csv", sep=";")
xdata = data.loc[:, ['alcohol']].values
ydata = data.loc[:, ['quality']].values
ave_x=0
ave_y=0
x_num=0 
y_num=0
A1=0
A2=0

for temp_x in xdata:
    ave_x +=temp_x
    x_num+=1

for temp_y in xdata:
    ave_y +=temp_y
    y_num+=1

ave_x=ave_x/x_num #xの平均値を求める
ave_y=ave_y/x_num #yの平均値を求める

for i in range(1598):
    A1+=(xdata[i]-ave_x)*(ydata[i]-ave_y)
    A2+=(xdata[i]-ave_x)*(xdata[i]-ave_x)

a=A1/A2
print('係数:a=')
print(a)

print('切片:b=')
print(ave_y-a*ave_x)




