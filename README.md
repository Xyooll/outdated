# Xyool Backup Repository

> **Recovery copy available.**
>
> Stable pointer: `backup/xyool-latest`  
> Frozen snapshot: `backup/xyool-critical-2026-09-25`  
> Backup source: `Xyooll/Xyool@4137f4ee45b5ebb928c83361e98d1d54a6aceef8`
>
> The original contents of this repository's pre-backup `main` are preserved at:
> `archive/pre-xyool-backup-2026-09-25`
>
> Open `BACKUP-README.md` on the backup branch for recovery scope, verification, and omissions.

---

## Previous README

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
