import streamlit as st

st.set_page_config(page_title="Crypto Dashboard Project", layout="wide")

st.title("Cryptocurrency Time Series Analysis Project")

st.markdown("""
### College Mini Project

This project analyzes cryptocurrency prices using time series and machine learning techniques.

**Modules included:**
- Historical Price Analysis  
- Moving Averages  
- Daily Returns  
- Volatility  
- High–Low Analysis  
- ARIMA Forecast  
- LSTM Forecast  
- Model Comparison  
- Summary Dashboard  

**Technologies Used:**
- CoinGecko API (Data Collection)  
- Pandas (Preprocessing)  
- Feature Engineering (Lag, Rolling Mean, Volatility)  
- ARIMA (Statistical Forecasting)  
- Dummy LSTM (Deep Learning Simulation)  
- Model Evaluation (MAE, RMSE, MAPE)  
- SQLite (Data Storage)  
- Logging (Error Tracking)  
- Streamlit (Dashboard)  

Use the sidebar to navigate through different dashboards.
""")

st.success("Select a dashboard from the left sidebar 👈")
