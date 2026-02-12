import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("Daily Returns Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

data["Daily Return"] = data["Close"].pct_change() * 100

st.subheader("Daily Percentage Returns")
st.line_chart(data.set_index("Date")["Daily Return"])
