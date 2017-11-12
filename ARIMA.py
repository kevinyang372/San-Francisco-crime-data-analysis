import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data
from category_classification import transform_category

file = load_data('train.csv')

from datetime import datetime, timedelta

time = []
for i in file['Dates']:
    i = i[:16]
    a = pd.datetime.strptime(i,'%Y-%m-%d %H:%M')
    time.append(a)

curr = time[0] - timedelta(hours=1)
ptime=[]
sumtime = []
tstamp = []
k = 0

while k < len(time):
    temp = []
    while k < len(time) and time[k] > curr:
        temp.append(time[k])
        k = k + 1
    curr -= timedelta(hours=1)
    if temp != []:
        tstamp.append(curr)
        ptime.append(temp)
        sumtime.append(len(temp))

time = pd.Series(sumtime,index=tstamp)

from statsmodels.tsa.arima_model import ARIMA
time = [float(i) for i in time]
time = pd.Series(time,index=tstamp)

model = ARIMA(time, order=(3, 1, 5))  
results_AR = model.fit(disp=-1)

print(results_AR.summary())
# plot residual errors
residuals = pd.DataFrame(results_AR.resid)
residuals.plot(kind='kde')
print(residuals.describe())

predictions_ARIMA_diff = pd.Series(results_AR.fittedvalues, copy=True)
for i in range(len(predictions_ARIMA_diff)):
    predictions_ARIMA_diff[i] = -predictions_ARIMA_diff[i]
sum = 0
for i in range(len(predictions_ARIMA_diff)):
    sum += predictions_ARIMA_diff[i] - time[i]
avg_add = -sum / len(time)

for i in range(len(predictions_ARIMA_diff)):
    predictions_ARIMA_diff[i] += avg_add

sum = 0
for i in range(len(predictions_ARIMA_diff)):
    sum += (predictions_ARIMA_diff[i] - time[i])**2
print('RMSE: ',np.sqrt(sum / len(time)))

