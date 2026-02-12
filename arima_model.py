import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_forecast(data, steps=30):
    model = ARIMA(data["Close"], order=(5, 1, 0))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=steps)

    last_date = data["Date"].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=steps+1, freq="D")[1:]

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast": forecast.values
    })

    return forecast_df
