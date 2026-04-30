# Crypto Sentiment Analysis

## Objective
Analyze trader performance vs market sentiment. This project combines historical trading data with the Fear and Greed Index to identify patterns and performance metrics under various market conditions.

## Features
- **Data Loading**: Loads historical trade data and market sentiment index.
- **Preprocessing**: Cleans and aligns data points to ensure temporal consistency.
- **Feature Engineering**: Derives additional metrics like win rates and profit indicators.
- **Analysis**: Generates summary statistics by sentiment classification.
- **Visualization**: Produces Box plots for PnL distributions and line charts for daily PnL trends.

## Project Structure
- `src/`: Source code modules (`data_loader.py`, `preprocessing.py`, `feature_engineering.py`, `analysis.py`, `visualization.py`).
- `data/`: Contains raw and processed data.
- `outputs/`: Generated plots and reports.
- `main.py`: Main entry point for the analysis script.

## Installation
Ensure you have Python installed. Install dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
Run the main script to process the data, perform the analysis, and generate visualizations:
```bash
python main.py
```
The script will output sentiment analysis to the console and save the plots (distribution and trend graphs) to `outputs/plots/`.
