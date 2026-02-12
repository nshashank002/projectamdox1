def preprocess(data):
    data = data.copy()

    if data.empty:
        return data

    data["Close"] = data["Close"].astype(float)
    data.dropna(inplace=True)

    return data
