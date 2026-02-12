import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("Moving Averages Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

data["MA7"] = data["Close"].rolling(7).mean()
data["MA30"] = data["Close"].rolling(30).mean()

st.subheader("Price with Moving Averages")
st.line_chart(data.set_index("Date")[["Close", "MA7", "MA30"]])
