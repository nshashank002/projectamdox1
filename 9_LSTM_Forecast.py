import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess
from lstm_model import train_lstm, prepare_lstm_data

st.title("LSTM Forecast Dashboard (Python 3.13 Compatible)")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

model, scaler = train_lstm(data)
X, y, _ = prepare_lstm_data(data)

pred = model.predict(X).flatten()

st.subheader("Dummy LSTM Predictions")
st.line_chart(pred)

st.success("Dummy LSTM model executed successfully (no TensorFlow needed).")
