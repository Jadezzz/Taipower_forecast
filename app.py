import pandas as pd
import numpy as np
from fbprophet import Prophet

# Load simplified datasets
data_2014_2016 = pd.read_csv('./datasets/2014_2016_simple.csv')
data_2017 = pd.read_csv('./datasets/2017_simple.csv')
data_2018 = pd.read_csv('./datasets/2018_simple.csv')
data_2019 = pd.read_csv('./datasets/2019_simple.csv')
holidays = pd.read_csv('./datasets/holidays.csv')

# Change the dataset to the specific format for Prophet
data = pd.DataFrame()
all_data = pd.concat([data_2014_2016, data_2017, data_2018, data_2019], ignore_index = True, sort=False)
all_data.drop('Unnamed: 0', axis=1, inplace=True)

data['ds'] = pd.to_datetime(all_data['date'], format='%Y%m%d').dt.strftime("%Y-%m-%d")
data['y'] = all_data['peak_load']

# Create a model
m = Prophet(holidays=holidays)
m.fit(data)

# Make prediction for next 8 days
future = m.make_future_dataframe(periods=8)

# Predict
forecast = m.predict(future)

output = pd.DataFrame()
output['date'] = forecast['ds'].tail(7).dt.strftime('%Y%m%d')
output['peak_load(MW)'] = forecast['yhat'].tail(7).round(0).astype(int)
output.reset_index(drop=True, inplace=True)
output.to_csv('submission.csv', index=False)