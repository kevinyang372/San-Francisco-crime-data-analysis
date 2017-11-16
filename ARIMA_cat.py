import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data

file = load_data('train.csv')

from datetime import datetime, timedelta

time = []
for i in file['Dates']:
    i = i[:16]
    a = pd.datetime.strptime(i,'%Y-%m-%d %H:%M')
    time.append(a)

Category_chosen = ["LARCENY/THEFT","OTHER OFFENSES","ASSAULT","DRUG/NARCOTIC","SEX OFFENSES FORCIBLE"]

processed = []
for i in Category_chosen:
    temp = []
    for t in range(len(file["Category"])):
        if file["Category"][t] == i:
            temp.append(1)
        else:
            temp.append(0)
    processed.append(temp)

ptime_s = []
sumtime_s = []

for i in processed:
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
    
    ptime_s.append(ptime)
    sumtime_s.append(sumtime)

t1 = [float(i) for i in sumtime_s[0]]
t2 = [float(i) for i in sumtime_s[1]]
t3 = [float(i) for i in sumtime_s[2]]
t4 = [float(i) for i in sumtime_s[3]]
t5 = [float(i) for i in sumtime_s[4]]

time_t = pd.Series(t1,index=tstamp)
time_o = pd.Series(t2,index=tstamp)
time_a = pd.Series(t3,index=tstamp)
time_d = pd.Series(t4,index=tstamp)
time_s = pd.Series(t5,index=tstamp)

from statsmodels.tsa.arima_model import ARIMA
def __getnewargs__(self):
    return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))
ARIMA.__getnewargs__ = __getnewargs__

model = ARIMA(time_t, order=(3, 1, 5))  
model_fit = model.fit(disp=-1)
model_fit.save('Theft.pkl')
model = ARIMA(time_o, order=(3, 1, 5))  
model_fit = model.fit(disp=-1)
model_fit.save('Offenses.pkl')
model = ARIMA(time_a, order=(3, 1, 5))  
model_fit = model.fit(disp=-1)
model_fit.save('Assault.pkl')
model = ARIMA(time_d, order=(3, 1, 5))  
model_fit = model.fit(disp=-1)
model_fit.save('Drug.pkl')
model = ARIMA(time_s, order=(3, 1, 5))  
model_fit = model.fit(disp=-1)
model_fit.save('Sexoffense.pkl')