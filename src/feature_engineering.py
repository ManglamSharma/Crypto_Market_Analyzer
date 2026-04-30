def create_features(data):
    data["win"] = data["closed_pnl"] > 0
    return data