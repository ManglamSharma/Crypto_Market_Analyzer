def sentiment_analysis(data):
    result = data.groupby("classification").agg({
        "closed_pnl": ["mean", "sum", "count"],
        "win": "mean"
    })
    return result