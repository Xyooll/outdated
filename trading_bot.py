import os
import requests
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def fetch_market_data(symbol="BTCUSDT", interval="1h", limit=500, fallback="sample_data.csv"):
    """Fetch historical market data from Binance.

    If the request fails (for example, due to network restrictions),
    data will be loaded from ``fallback`` CSV instead.
    """
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        df = pd.DataFrame(data, columns=[
            "OpenTime", "Open", "High", "Low", "Close", "Volume",
            "CloseTime", "QuoteAssetVolume", "NumTrades", "TakerBuyBase", "TakerBuyQuote", "Ignore"])
        df["Open"] = df["Open"].astype(float)
        df["High"] = df["High"].astype(float)
        df["Low"] = df["Low"].astype(float)
        df["Close"] = df["Close"].astype(float)
        df["Volume"] = df["Volume"].astype(float)
        return df
    except Exception as e:
        print("Failed to fetch data from Binance:", e)
        if os.path.exists(fallback):
            print(f"Loading data from {fallback}")
            return pd.read_csv(fallback)
        else:
            raise RuntimeError("No data available") from e


def prepare_features(df):
    df['MA_fast'] = df['Close'].rolling(window=5).mean()
    df['MA_slow'] = df['Close'].rolling(window=20).mean()
    df['Return'] = df['Close'].pct_change()
    df['Signal'] = (df['MA_fast'] > df['MA_slow']).astype(int)
    df = df.dropna()
    X = df[['MA_fast', 'MA_slow', 'Return']]
    y = df['Signal'].shift(-1).dropna()
    X = X.iloc[:-1]
    return X, y


def train_or_update_model(X, y, model_path="model.pkl"):
    """Train a new model or update an existing one with new data."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    if os.path.exists(model_path):
        model = joblib.load(model_path)
        model.partial_fit(X_train, y_train)
    else:
        model = SGDClassifier(loss="log_loss", random_state=42)
        model.partial_fit(X_train, y_train, classes=np.array([0, 1]))

    preds = model.predict(X_test)
    print("Model accuracy:", accuracy_score(y_test, preds))
    joblib.dump(model, model_path)
    return model


def generate_signal(model, df):
    latest = df.iloc[-1]
    features = np.array([[latest['MA_fast'], latest['MA_slow'], latest['Return']]])
    signal = model.predict(features)[0]
    if signal == 1:
        return "BUY"
    else:
        return "SELL"


def main():
    df = fetch_market_data()
    X, y = prepare_features(df)
    model = train_or_update_model(X, y)
    signal = generate_signal(model, df)
    print("Generated signal:", signal)


if __name__ == "__main__":
    main()
