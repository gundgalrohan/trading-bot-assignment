import argparse
import os
import sys

from dotenv import load_dotenv

from bot.client import BinanceClient
from bot.logging_config import setup_logger
from bot.orders import place_order, print_order_response, print_order_summary
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)

load_dotenv()
logger = setup_logger("cli")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", dest="order_type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity e.g. 0.01")
    parser.add_argument("--price", required=False, default=None, help="Price (required for LIMIT orders)")
    return parser.parse_args()


def main():
    args = parse_args()

    # Validate inputs
    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.order_type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)
    except ValueError as e:
        print(f"\n❌ Validation Error: {e}\n")
        logger.error(f"Validation Error: {e}")
        sys.exit(1)

    # Load API credentials
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("\n❌ Error: BINANCE_API_KEY and BINANCE_API_SECRET must be set in .env file\n")
        logger.error("Missing API credentials in environment.")
        sys.exit(1)

    # Print order summary
    print_order_summary(symbol, side, order_type, quantity, price)

    # Place order
    try:
        client = BinanceClient(api_key, api_secret)
        response = place_order(client, symbol, side, order_type, quantity, price)
        print_order_response(response)
    except RuntimeError as e:
        print(f"\n❌ Order Failed: {e}\n")
        logger.error(f"Order Failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
