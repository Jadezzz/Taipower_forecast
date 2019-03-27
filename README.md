# Taipower Forecast
## Description

Given past data from Taipower, predict next 7 days' 'peak load'

## Dependencies

* numpy
* pandas
* scikit-learn
* pystan
* fbprophet

Type in command to install above:

``` pip install -r requeirments.txt ```

## Run

``` python3 app.py ```

## Result

The result will store in ```submission.csv```

Example of ```submission.csv```
```
date,peak_load(MW)
20190328,28714
20190329,28487
20190330,25660
20190331,24482
20190401,28379
20190402,28775
20190403,28821
```

## More information in notebook
https://nbviewer.jupyter.org/github/Jadezzz/Taipower_forecast/blob/master/forecasting.ipynb