from typing import Any, Dict, Optional

from .client import BinanceClient
from .logging_config import setup_logger

logger = setup_logger("orders")


def place_order(
    client: BinanceClient,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float] = None,
) -> Dict[str, Any]:
    logger.info(
        f"Placing {order_type} {side} order | Symbol: {symbol} | Qty: {quantity}"
        + (f" | Price: {price}" if price else "")
    )

    response = client.place_order(
        symbol=symbol,
        side=side,
        order_type=order_type,
        quantity=quantity,
        price=price,
    )

    logger.info(
        f"Order placed successfully | OrderId: {response.get('orderId')} | "
        f"Status: {response.get('status')} | ExecutedQty: {response.get('executedQty')}"
    )

    return response


def print_order_summary(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: Optional[float],
) -> None:
    print("\n" + "=" * 45)
    print("         ORDER REQUEST SUMMARY")
    print("=" * 45)
    print(f"  Symbol     : {symbol}")
    print(f"  Side       : {side}")
    print(f"  Type       : {order_type}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("=" * 45)


def print_order_response(response: Dict[str, Any]) -> None:
    print("\n" + "=" * 45)
    print("         ORDER RESPONSE DETAILS")
    print("=" * 45)
    print(f"  Order ID   : {response.get('orderId', 'N/A')}")
    print(f"  Status     : {response.get('status', 'N/A')}")
    print(f"  Exec Qty   : {response.get('executedQty', 'N/A')}")
    print(f"  Avg Price  : {response.get('avgPrice', 'N/A')}")
    print(f"  Symbol     : {response.get('symbol', 'N/A')}")
    print(f"  Side       : {response.get('side', 'N/A')}")
    print(f"  Type       : {response.get('type', 'N/A')}")
    print("=" * 45)
    print("  ✅ Order placed successfully!")
    print("=" * 45 + "\n")
