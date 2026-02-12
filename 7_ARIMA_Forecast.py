import streamlit as st
from data_fetch import fetch_crypto
from preprocessing import preprocess
from arima_model import arima_forecast
from feature_engineering import add_features
from data_split import train_test_split
from evaluation import mae, rmse, mape
from logger import log_info, log_error

st.title("ARIMA Forecast Dashboard (Enhanced)")

coin = st.selectbox("Select Cryptocurrency", ["bitcoin", "ethereum", "dogecoin"])

raw = fetch_crypto(coin, days=365)

if raw.empty:
    st.error("Failed to fetch data from CoinGecko API.")
else:
    data = preprocess(raw)

    # ✅ NOW data exists
    features = add_features(data)
    train, test = train_test_split(features)

    log_info("Feature engineering and train-test split completed.")

    st.subheader("Last 30 Days Actual Price")
    last_data = data.tail(30)
    st.line_chart(last_data.set_index("Date")["Close"])

    st.subheader("ARIMA Forecast (Next 30 Days)")

    try:
        forecast_df = arima_forecast(train)

        if forecast_df.empty:
            st.warning("Forecast could not be generated.")
        else:
            st.line_chart(forecast_df.set_index("Date")["Forecast"])

            # -------- Evaluation --------
            actual = test["Close"].values[:30]
            predicted = forecast_df["Forecast"].values[:30]

            st.subheader("Model Evaluation (ARIMA)")
            st.write("MAE:", mae(actual, predicted))
            st.write("RMSE:", rmse(actual, predicted))
            st.write("MAPE:", mape(actual, predicted), "%")

    except Exception as e:
        log_error(str(e))
        st.error("ARIMA model failed.")
        st.write("Reason:", e)
