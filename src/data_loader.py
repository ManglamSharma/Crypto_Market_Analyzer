import pandas as pd

def load_data(trades_path, sentiment_path):
    trades = pd.read_csv(trades_path)
    sentiment = pd.read_csv(sentiment_path)
    return trades, sentiment