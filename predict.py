from statsmodels.tsa.arima_model import ARIMAResults
from location_based_ARIMA import run
from datasource import load_data

file = load_data("train.csv")

cat = input("input the category you want to predict (Theft, Assault, Drug, Sex Offenses, Other Offense)")
name = cat + '.pkl'

location_x = float(input('latitude'))
location_y = float(input('longtitude'))

possibility = run(location_x,location_y,file)

model = ARIMAResults.load(name)
raw = model.forecast()[0]

print("The possibility of crime is: ", raw*possibility*100, "%")

