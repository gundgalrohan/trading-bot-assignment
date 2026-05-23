# 🤖 Binance Futures Testnet Trading Bot

A Python CLI tool to place Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## 📁 Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic & output formatting
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging setup
├── logs/
│   └── trading_bot.log    # Auto-generated log file
├── cli.py                 # CLI entry point
├── .env.example           # Environment variable template
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Steps

### 1. Clone / Download the project

```bash
git clone https://github.com/your-username/trading_bot.git
cd trading_bot
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Binance Futures Testnet

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com)
2. Register / Log in
3. Generate API Key & Secret
4. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

5. Fill in your credentials in `.env`:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

---

## 🚀 How to Run

### Place a MARKET BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a MARKET SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.01
```

### Place a LIMIT BUY order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 60000
```

### Place a LIMIT SELL order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 68000
```

---

## 📋 Sample Output

```
=============================================
         ORDER REQUEST SUMMARY
=============================================
  Symbol     : BTCUSDT
  Side       : BUY
  Type       : MARKET
  Quantity   : 0.01
=============================================

=============================================
         ORDER RESPONSE DETAILS
=============================================
  Order ID   : 389451
  Status     : FILLED
  Exec Qty   : 0.01
  Avg Price  : 67345.20
  Symbol     : BTCUSDT
  Side       : BUY
  Type       : MARKET
=============================================
  ✅ Order placed successfully!
=============================================
```

---

## 📝 Logging

All API requests, responses, and errors are logged to:

```
logs/trading_bot.log
```

Log format:
```
YYYY-MM-DD HH:MM:SS | LEVEL | module | message
```

---

## ⚠️ Assumptions

- Only USDT-M Futures Testnet is supported
- Minimum quantity depends on the symbol (e.g. 0.001 BTC for BTCUSDT)
- LIMIT orders use `timeInForce = GTC` (Good Till Cancelled) by default
- API credentials must be stored in a `.env` file (never hardcoded)

---

## 🛠️ Tech Stack

- Python 3.x
- `requests` — HTTP API calls
- `python-dotenv` — Environment variable management
- `argparse` — CLI argument parsing

---

Built for Primetrade.ai – Python Developer Intern Assignment
