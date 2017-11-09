raw_data <- read.csv('train.csv')

myval <- c('Dates','Category','DayOfWeek','PdDistrict')
data <- raw_data[myval]