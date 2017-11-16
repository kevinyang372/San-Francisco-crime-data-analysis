import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datasource import load_data
from category_classification import transform_category

file = load_data('train.csv')

time_data_hour = []
time_data_month = []
time_data_year = []
for i in file['Dates']:
    hour = i[11:16]
    year = i[:4]
    if(year != '2015'):
        month = i[5:7]
        b = pd.datetime.strptime(month,'%m')
        time_data_month.append(b)
    a = pd.datetime.strptime(hour,'%H:%M')
    c = pd.datetime.strptime(year,'%Y')
    time_data_hour.append(a)
    time_data_year.append(c)



hour = plt.hist(time_data_hour,bins=24)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = hour[0]
mean_value = np.mean(hour[0])
index = np.arange(0,24)
ax.plot(index,value_count)
plt.xticks(index)
plt.title("Total Number of Crime Over 24 Hours Time Span")
plt.xlabel("Hour")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



month = plt.hist(time_data_month,bins=12)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = month[0]
mean_value = np.mean(value_count)
index = np.arange(1,13)
ax.plot(index,value_count,color="orange")
plt.xticks(index)
plt.title("Total Number of Crime Over 12 Months (2003-1015)")
plt.xlabel("Month")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



year = plt.hist(time_data_year,bins=13)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = year[0][:12]
mean_value = np.mean(value_count)
index = np.arange(2003,2015)
ax.plot(index,value_count,color="darkgreen")
plt.xticks(index)
plt.title("Total Number of Crime From 2003 to 2014")
plt.xlabel("Year")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



new_data = transform_category(file['Category'])
time_data_hour_a = []
time_data_month_a = []
time_data_year_a = []
for i in range(len(file['Dates'])):
    if new_data[i] == 'ASSAULT':
        t = file['Dates'][i]
        hour = t[11:16]
        year = t[:4]
        if(year != "2015"):
            month = t[5:7]
            b = pd.datetime.strptime(month,'%m')
            time_data_month_a.append(b)
        a = pd.datetime.strptime(hour,'%H:%M')
        c = pd.datetime.strptime(year,'%Y')
        time_data_hour_a.append(a)
        time_data_year_a.append(c)


hour_a = plt.hist(time_data_hour_a,bins=24)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = hour_a[0]
mean_value = np.mean(hour_a[0])
index = np.arange(0,24)
ax.plot(index,value_count)
plt.xticks(index)
plt.title("Total Number of Assault Crime Over 24 Hours Time Span")
plt.xlabel("Hour")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



month_a = plt.hist(time_data_month_a,bins=12)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = month_a[0]
mean_value = np.mean(month_a[0])
index = np.arange(1,13)
ax.plot(index,value_count)
plt.xticks(index)
plt.title("Total Number of Assault Crime Over 12 Month")
plt.xlabel("Hour")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



year_a = plt.hist(time_data_year_a,bins=13)
plt.show()

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
value_count = year_a[0][:12]
mean_value = np.mean(value_count)
index = np.arange(2003,2015)
ax.plot(index,value_count,color="darkgreen")
plt.xticks(index)
plt.title("Total Number of Assault Crime From 2003 to 2014")
plt.xlabel("Year")
plt.ylabel("Number of Crime")
plt.axhline(y=mean_value,linestyle='--',color='gray',label="Mean")
plt.legend()
plt.show()



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

fig = plt.figure(figsize=(15, 5))

ax = fig.add_subplot(111)
ax.plot(tstamp,sumtime)
plt.xlabel("Time")
plt.ylabel("Number of Crime")
plt.show()