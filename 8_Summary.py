import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess

st.title("Summary Dashboard")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)
data = preprocess(raw)

st.subheader("Project Summary")

if data.empty:
    st.error("No data available. Please refresh or try again later.")
else:
    avg_price = float(data["Close"].mean())
    max_price = float(data["Close"].max())
    min_price = float(data["Close"].min())
    total_points = len(data)

    st.write("**Total Data Points:**", total_points)
    st.write("**Average Price:**", f"${avg_price:,.2f}")
    st.write("**Maximum Price:**", f"${max_price:,.2f}")
    st.write("**Minimum Price:**", f"${min_price:,.2f}")

    st.success("This completes the cryptocurrency analysis project 🎉")
