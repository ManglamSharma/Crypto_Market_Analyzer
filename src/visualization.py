import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def plot_pnl_distribution(data, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(8, 5))
    sns.boxplot(x="classification", y="closed_pnl", data=data)

    plt.title("PnL Distribution by Sentiment")
    plt.xticks(rotation=30)

    path = os.path.join(output_dir, "pnl_distribution.png")
    plt.savefig(path)
    plt.close()

    print("✅ Saved:", path)


def plot_pnl_trend(data, output_dir):
    print("🔥 Running trend plot...")

    data["date"] = pd.to_datetime(data["date"], errors="coerce")
    data = data.dropna(subset=["date", "classification", "closed_pnl"])

    trend = data.groupby(["date", "classification"])["closed_pnl"].sum().reset_index()

    if trend.empty:
        print("❌ No data for trend plot")
        return

    plt.figure(figsize=(12, 6))

    sns.lineplot(
        data=trend,
        x="date",
        y="closed_pnl",
        hue="classification"
    )

    plt.title("Daily PnL Trend by Market Sentiment")
    plt.xticks(rotation=45)

    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "pnl_trend.png")
    plt.savefig(path)
    plt.close()

    print("✅ Trend graph saved at:", path)