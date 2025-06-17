# AI Trading Bot

This repository contains a simple example of an AI-driven trading bot written in Python. The bot fetches historical price data from Binance and trains a random forest model to generate buy/sell signals.

If the Binance API cannot be reached (for example, due to network restrictions), the script falls back to a small sample dataset included in this repository (`sample_data.csv`).

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the bot with:

```bash
python trading_bot.py
```

The script will output the model accuracy and a generated trading signal.
