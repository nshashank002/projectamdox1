import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("Volatility Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

data["Volatility"] = data["Close"].rolling(30).std()

st.subheader("30-Day Rolling Volatility")
st.line_chart(data.set_index("Date")["Volatility"])
