import pandas as pd

def load_data(data_name):
	file = pd.read_csv(data_name)
	return file