import pandas as pd

def preprocess_data(trades, sentiment):
    # ✅ Normalize column names (VERY IMPORTANT)
    trades.columns = trades.columns.str.strip().str.lower().str.replace(" ", "_")
    sentiment.columns = sentiment.columns.str.strip().str.lower().str.replace(" ", "_")

    # ✅ Correct date parsing (FIX YOUR ERROR)
    trades["timestamp_ist"] = pd.to_datetime(
        trades["timestamp_ist"],
        dayfirst=True,     # 🔥 IMPORTANT FIX
        errors="coerce"    # avoids crash if bad values
    )

    sentiment["date"] = pd.to_datetime(sentiment["date"], errors="coerce")

    # ✅ Create common date column
    trades["date"] = trades["timestamp_ist"].dt.date
    sentiment["date"] = sentiment["date"].dt.date

    return trades, sentiment