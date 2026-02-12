import streamlit as st

st.title("Home Dashboard")

st.markdown("""
### Cryptocurrency Time Series Analysis Project

This project analyzes cryptocurrency prices using time series analysis and machine learning techniques.

**Main Objectives:**
- Analyze historical price data  
- Study trends and volatility  
- Forecast future prices using ARIMA  
- Forecast future prices using LSTM  
- Compare ARIMA vs LSTM models  
- Evaluate models using MAE, RMSE, and MAPE  
- Apply feature engineering (lag values, rolling mean, volatility)  
- Include sentiment analysis (market mood)  
- Store data in a database (SQLite)  
- Track errors using logging  

**Tools Used:**
- CoinGecko API (Primary Data Source)  
- Yahoo Finance (Fallback Data Source)  
- Pandas (Preprocessing)  
- Feature Engineering Module  
- ARIMA Model (Statistical Forecasting)  
- Dummy LSTM (Deep Learning Simulation)  
- Model Evaluation (MAE, RMSE, MAPE)  
- SQLite (Data Storage)  
- Logging (Error Tracking)  
- Streamlit (Dashboard)  

Use the sidebar to explore different dashboards.
""")

st.success("Welcome to the Crypto Analytics Dashboard 🚀")
