# San_Francisco_Crime_Data_Analysis
From 1934 to 1963, San Francisco was infamous for housing some of the world's most notorious criminals on the inescapable island of Alcatraz.

Today, the city is known more for its tech scene than its criminal past. But, with rising wealth inequality, housing shortages, and a proliferation of expensive digital toys riding BART to work, there is no scarcity of crime in the city by the bay.

The project aims to visualize the crime data record from 2004 to 2016 and helps to give predictions on the possible danger one may meet given their location and time to lower the harm of crimes to citizens and tourists in San Francisco.

Several models are implemented to achieve that goal. Including random decision tree, nonlinear SVC and ARIMA time series prediction. Currently, the one with highest test precision and recall is ARIMA model. The following is description of files included in the project:

ARIMA.py: A detailed walk-through of statistic analysis, parameter selection and model training<br>
ARIMA_cat.py: Training models based on different types of crime<br>
location_based_ARIMA.py: Adding location based features to the model<br>
predict.py: Running models<br>
train.csv: Database for model training<br>

The original data source is from Kaggle (https://www.kaggle.com/c/sf-crime/data)
