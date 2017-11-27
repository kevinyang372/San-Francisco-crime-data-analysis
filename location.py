import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data

#location blurring
def examine_position(i,previous_list,file):
    for k in previous_list:
        if np.abs(k[0]-file["X"][i]) < 0.003 and np.abs(k[1]-file["Y"][i]) < 0.003:
            k[2] += 1
            return
    previous_list.append([file["X"][i],file["Y"][i],1])

#determine the location of the input
def determine_possibility(x,y,blurred_list):
    for i in blurred_list:
        if np.abs(x-i[0]) < 0.003 and np.abs(y-i[1]) < 0.003:
            possibility = i[2]/10000
            return possibility
    return 0

def run(x,y,file):
    blurred_list=[]
    for i in range(10000):
        examine_position(i,blurred_list,file)
    return determine_possibility(x,y,blurred_list)

