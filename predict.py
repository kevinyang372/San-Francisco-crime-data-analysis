from statsmodels.tsa.arima_model import ARIMAResults
from location import run
from datasource import load_data

#load dataset
file = load_data("train.csv")

#take input
cat = input("input the category you want to predict (Theft, Assault, Drug, Sex Offenses, Other Offenses)")

if cat.lower() == "theft":
	cat = "Theft"
elif cat.lower() == "assault":
	cat = "Assault"
elif cat.lower() == "drug":
	cat = "Drug"
elif cat.lower() == "sex offenses":
	cat = "Sexoffense"
elif cat.lower() == "other offenses":
	cat = "Offenses"

#find model
name = cat + '.pkl'

#get latitude and longtitude
location_x = float(input('latitude'))
location_y = float(input('longtitude'))

#get location possibility
possibility = run(location_x,location_y,file)

#predict
model = ARIMAResults.load(name)
raw = model.forecast()[0]

print("The possibility of crime is: ", raw*possibility*100, "%")

