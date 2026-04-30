import pandas as pd
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.feature_engineering import create_features
from src.analysis import sentiment_analysis
from src.visualization import plot_pnl_distribution, plot_pnl_trend


def main():
    # Load data
    trades, sentiment = load_data(
        "data/raw/historical_data.csv",
        "data/raw/fear_greed_index.csv"
    )

    # Preprocess
    trades, sentiment = preprocess_data(trades, sentiment)

    # Merge
    merged = pd.merge(trades, sentiment, on="date", how="left")

    # Feature engineering
    merged = create_features(merged)

    # Analysis
    print("\n📊 Sentiment Analysis:\n")
    print(sentiment_analysis(merged))

    # Visualization
    plot_pnl_distribution(merged, "outputs/plots")
    plot_pnl_trend(merged, "outputs/plots")

    # Save processed data
    merged.to_csv("data/processed/merged_data.csv", index=False)


if __name__ == "__main__":
    main()