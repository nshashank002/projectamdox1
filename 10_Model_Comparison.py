import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess
from feature_engineering import add_features
from data_split import train_test_split
from arima_model import arima_forecast
from lstm_model import train_lstm, prepare_lstm_data
from evaluation import mae, rmse, mape

st.title("Model Comparison Dashboard (Python 3.13 Compatible)")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

features = add_features(data)
train, test = train_test_split(features)

# ---------- ARIMA ----------
forecast_df = arima_forecast(train)
arima_pred = forecast_df["Forecast"].values[:len(test)]
arima_actual = test["Close"].values[:len(arima_pred)]

arima_mae = mae(arima_actual, arima_pred)
arima_rmse = rmse(arima_actual, arima_pred)
arima_mape = mape(arima_actual, arima_pred)

st.subheader("ARIMA Metrics")
st.write("MAE:", arima_mae)
st.write("RMSE:", arima_rmse)
st.write("MAPE:", arima_mape, "%")

# ---------- Dummy LSTM ----------
model, _ = train_lstm(train)
X_test, y_test, _ = prepare_lstm_data(test)

lstm_pred = model.predict(X_test).flatten()
lstm_actual = y_test

lstm_mae = mae(lstm_actual, lstm_pred)
lstm_rmse = rmse(lstm_actual, lstm_pred)
lstm_mape = mape(lstm_actual, lstm_pred)

st.subheader("Dummy LSTM Metrics")
st.write("MAE:", lstm_mae)
st.write("RMSE:", lstm_rmse)
st.write("MAPE:", lstm_mape, "%")

# ---------- Final Table ----------
st.subheader("Final Comparison")

st.table({
    "Model": ["ARIMA", "Dummy LSTM"],
    "MAE": [arima_mae, lstm_mae],
    "RMSE": [arima_rmse, lstm_rmse],
    "MAPE (%)": [arima_mape, lstm_mape]
})
