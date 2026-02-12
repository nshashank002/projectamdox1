import pandas as pd

def add_features(data):
    df = data.copy()

    # Lag features
    df["lag_1"] = df["Close"].shift(1)
    df["lag_7"] = df["Close"].shift(7)

    # Rolling features
    df["rolling_mean_7"] = df["Close"].rolling(7).mean()
    df["rolling_vol_7"] = df["Close"].rolling(7).std()

    # Fake volume (CoinGecko free API doesn't provide clean volume history)
    df["Volume"] = df["Close"] * 0.1  

    df.dropna(inplace=True)
    return df
