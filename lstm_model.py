import numpy as np

def prepare_lstm_data(data, lookback=10):
    values = data["Close"].values.reshape(-1, 1)

    X, y = [], []
    for i in range(lookback, len(values)):
        X.append(values[i-lookback:i, 0])
        y.append(values[i, 0])

    X = np.array(X)
    y = np.array(y)

    return X, y, None


def train_lstm(data):
    mean_value = data["Close"].mean()

    class DummyModel:
        def predict(self, X):
            return np.full((len(X), 1), mean_value)

    return DummyModel(), None
