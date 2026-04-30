import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# ==============================
# 📁 Project Structure
# ==============================
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "outputs/plots",
    "outputs/report"
]

files = {
    "src/__init__.py": "",

    "src/data_loader.py": """import pandas as pd

def load_data(trades_path, sentiment_path):
    trades = pd.read_csv(trades_path)
    sentiment = pd.read_csv(sentiment_path)
    return trades, sentiment
""",

    "src/preprocessing.py": """import pandas as pd

def preprocess_data(trades, sentiment):
    trades["time"] = pd.to_datetime(trades["time"])
    sentiment["Date"] = pd.to_datetime(sentiment["Date"])

    trades["date"] = trades["time"].dt.date
    sentiment["date"] = sentiment["Date"].dt.date

    return trades, sentiment
""",

    "src/feature_engineering.py": """def create_features(data):
    data["win"] = data["closedPnL"] > 0
    return data
""",

    "src/analysis.py": """def sentiment_analysis(data):
    return data.groupby("Classification").agg({
        "closedPnL": ["mean", "sum"],
        "leverage": "mean",
        "win": "mean"
    })
""",

    "src/visualization.py": """import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_pnl_distribution(data, output_dir):
    plt.figure()
    sns.boxplot(x="Classification", y="closedPnL", data=data)
    plt.savefig(os.path.join(output_dir, "pnl_distribution.png"))
    plt.close()
""",

    "main.py": """import pandas as pd
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.analysis import sentiment_analysis
from src.visualization import plot_pnl_distribution

def main():
    trades, sentiment = load_data(
        "data/raw/historical_data.csv",
        "data/raw/fear_greed.csv"
    )

    trades, sentiment = preprocess_data(trades, sentiment)

    merged = pd.merge(trades, sentiment, on="date", how="left")
    merged = create_features(merged)

    print(sentiment_analysis(merged))

    plot_pnl_distribution(merged, "outputs/plots")

if __name__ == "__main__":
    main()
""",

    "requirements.txt": """pandas
numpy
matplotlib
seaborn
scikit-learn
""",

    "README.md": """# Crypto Sentiment Analysis

## Objective
Analyze trader performance vs market sentiment.

## Run
pip install -r requirements.txt
python main.py
"""
}


# ==============================
# 🛠️ Create Folders
# ==============================
for folder in folders:
    os.makedirs(folder, exist_ok=True)


# ==============================
# 🛠️ Create Files
# ==============================
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


print("✅ Project structure created successfully!")