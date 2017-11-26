import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data
from category_classification import transform_category

#load data
file = load_data('train.csv')

from datetime import datetime, timedelta

#convert string into timestamp
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

#separate time stamps into time intervals of one hour
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

#dataset
from statsmodels.tsa.arima_model import ARIMA
time = [float(i) for i in time]
time = pd.Series(time,index=tstamp)

#separate training-test set split
size = int(len(time) - 100)
train, test = time[0:size], time[size:len(time)]
history = [x for x in train]
predictions = list()

#train ARIMA model
model = ARIMA(history, order=(3,1,5))
model_fit = model.fit(disp=0)

#forecast the next 100 pieces of data
output = model_fit.forecast(steps=100)[0]
output = [x for x in output]
test = [x for x in test]

fig = plt.figure(figsize=(10,5))

#plot the predicted vs. expected graph
ax = fig.add_subplot(111)
ax.plot(test,label="Observed")
ax.plot(output,label="Predicted")
plt.xlabel("Time")
plt.ylabel("Number of Crime")
plt.legend()
plt.show()

#save the ARIMA model
def __getnewargs__(self):
    return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))

ARIMA.__getnewargs__ = __getnewargs__

model_fit.save('model.pkl')