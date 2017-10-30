import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def filterdata(file):
    y_result = file["Category"].copy()
    y_result = transform_to_one_hot(y_result)
    Dates = file["Dates"].copy()
    Dates = transform_to_time(Dates)
    DaysOfWeek = file["DayOfWeek"].copy()
    DaysOfWeek = transform_to_one_hot(DaysOfWeek)
    District = file["PdDistrict"].copy()
    District = transform_to_one_hot(District)
    train_tr = np.column_stack((Dates,District))
    train_tr = np.column_stack((train_tr,DaysOfWeek))
    return y_result,train_tr

#Transform string into one hot arrays
def transform_to_one_hot(dataset):
    encoder = LabelBinarizer()
    new_dataset = encoder.fit_transform(dataset)
    return new_dataset

#Transform time from string to integers
def transform_to_time(dataset):
    num = []
    for i in dataset:
        temp = i[11:].split(':')
        temp = list(map(int,temp))
        num.append(temp[0]*60 + temp[1])
    return num