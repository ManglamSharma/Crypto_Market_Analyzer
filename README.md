# Crypto Sentiment Analysis

## Objective
The goal of this project is to analyze trader performance in relation to overall market sentiment. By combining historical trading data with sentiment indicators (such as the Fear & Greed Index), we aim to identify patterns in profitability, win rates, and leverage usage across different market sentiment classifications.

## Features
- **Data Loading**: Loads raw trading data and market sentiment data.
- **Preprocessing**: Cleans and aligns timestamps to merge datasets by date.
- **Feature Engineering**: Derives additional metrics like binary "win" indicators based on closed PnL.
- **Sentiment Analysis**: Aggregates trading performance (e.g., average PnL, leverage, and win rate) grouped by market sentiment classifications.
- **Visualization**: Generates visualizations, including:
  - Boxplots of PnL distribution by sentiment.
  - Line plots of daily PnL trends against market sentiment.

## Project Structure
```text
.
├── data/
│   ├── raw/                # Raw input data (historical_data.csv, fear_greed_index.csv)
│   └── processed/          # Cleaned and merged output datasets
├── notebooks/              # Jupyter notebooks for exploratory data analysis (EDA)
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Functions to load data from CSVs
│   ├── preprocessing.py    # Time-series alignment and preprocessing
│   ├── feature_engineering.py # Derived feature calculation
│   ├── analysis.py         # Sentiment-based aggregation and analysis
│   └── visualization.py    # Code to generate Matplotlib/Seaborn plots
├── outputs/
│   ├── plots/              # Generated visualizations (e.g., pnl_distribution.png)
│   └── report/             # Output analysis reports
├── main.py                 # Main execution script orchestrating the pipeline
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Installation
1. Clone the repository and navigate into it.
2. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main script to process the data, perform analysis, and generate visualizations:
```bash
python main.py
```

## Expected Outputs
- **Console**: Will print aggregated statistics and performance metrics grouped by market sentiment.
- **Data**: A processed and merged dataset will be saved at `data/processed/merged_data.csv`.
- **Plots**: Generated visualizations will be saved in `outputs/plots/`, including:
  - `pnl_distribution.png`: Boxplot of closed PnL grouped by sentiment.
  - `pnl_trend.png`: Line chart showing PnL trends over time.
