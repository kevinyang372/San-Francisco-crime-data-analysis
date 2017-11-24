import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data

file = load_data('train.csv')

def examine_position(i,previous_list):
    for k in previous_list:
        if np.abs(k[0]-file["X"][i]) < 0.003 and np.abs(k[1]-file["Y"][i]) < 0.003:
            k[2] += 1
            return
    previous_list.append([file["X"][i],file["Y"][i],1])

blurred_list=[]
for i in range(10000):
    examine_position(i,blurred_list)

x = []
y = []
c = []
for i in range(len(blurred_list)):
    x.append(blurred_list[i][0])
    y.append(blurred_list[i][1])
    c.append(blurred_list[i][2])
plt.scatter(x,y,c=c,s=10)
plt.show()

def determine_possibility(x,y,blurred_list):
    for i in blurred_list:
        if np.abs(x-i[0]) < 0.003 and np.abs(y-i[1]) < 0.003:
            possibility = i[2]/10000
            return possibility
    return 0

determine_possibility(file["X"][20010],file["Y"][20010],blurred_list)
print(file["X"][20010],file["Y"][20010])
