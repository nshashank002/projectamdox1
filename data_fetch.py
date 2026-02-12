import requests
import pandas as pd
import yfinance as yf
from logger import log_info, log_error

def fetch_crypto(coin_id="bitcoin", days=365):
    try:
        # ---------- Try CoinGecko ----------
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {"vs_currency": "usd", "days": days}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if "prices" not in data:
            raise ValueError("CoinGecko response missing prices")

        prices = data["prices"]
        df = pd.DataFrame(prices, columns=["timestamp", "Close"])
        df["Date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df[["Date", "Close"]]

        log_info(f"Fetched {len(df)} rows from CoinGecko for {coin_id}")
        return df

    except Exception as e:
        log_error(f"CoinGecko failed: {e}")
        log_info("Switching to Yahoo Finance fallback")

        # ---------- Fallback: Yahoo Finance ----------
        symbol_map = {
            "bitcoin": "BTC-USD",
            "ethereum": "ETH-USD",
            "dogecoin": "DOGE-USD"
        }

        symbol = symbol_map.get(coin_id, "BTC-USD")
        df = yf.download(symbol, period=f"{days}d", interval="1d", progress=False)

        if df.empty:
            log_error("Yahoo Finance also failed")
            return pd.DataFrame(columns=["Date", "Close"])

        df = df.reset_index()[["Date", "Close"]]
        log_info(f"Fetched {len(df)} rows from Yahoo Finance for {coin_id}")
        return df
