import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("Historical Prices Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

st.subheader("Historical Closing Prices")
st.line_chart(data.set_index("Date")["Close"])
