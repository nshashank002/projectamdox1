from prophet import Prophet

def prophet_forecast(data, days=30):
    df = data.rename(columns={'Date':'ds','Close':'y'})
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    return forecast
