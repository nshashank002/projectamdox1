import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("High–Low Analysis Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

if data.empty:
    st.error("No data available. Please refresh or try again later.")
else:
    # Force numeric conversion + safe float
    close_prices = data["Close"].astype(float)

    highest = float(close_prices.max())
    lowest = float(close_prices.min())

    st.subheader("Maximum and Minimum Prices")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Highest Price", f"${highest:,.2f}")

    with col2:
        st.metric("Lowest Price", f"${lowest:,.2f}")
