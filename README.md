# Binance Futures Testnet Trading Bot

A simple CLI tool to place MARKET and LIMIT orders on Binance Futures Testnet using Python.


## Project Structure
```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
├── logs/
│   └── trading_bot.log
├── cli.py
├── .env.example
├── requirements.txt
└── README.md
```

---

## Setup

1. Clone the repo and go into the folder
```bash
git clone https://github.com/username/trading-bot.git
cd trading-bot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Get your API keys from [testnet.binancefuture.com](https://testnet.binancefuture.com), then copy `.env.example` to `.env` and fill in your keys
```
BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret
```

---

## Usage

```bash
# Market BUY
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

# Limit SELL
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 72000
```

---

## Notes
- Only USDT-M Futures Testnet is supported
- LIMIT orders use GTC (Good Till Cancelled) by default
- Logs are saved to `logs/trading_bot.log`

---

Built for Primetrade.ai intern assignment
