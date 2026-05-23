import hashlib
import hmac
import time
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests

from .logging_config import setup_logger

logger = setup_logger("client")

BASE_URL = "https://testnet.binancefuture.com"


class BinanceClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": self.api_key})

    def _sign(self, params: Dict[str, Any]) -> str:
        query_string = urlencode(params)
        signature = hmac.new(
            self.api_secret.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
        return signature

    def _get_timestamp(self) -> int:
        return int(time.time() * 1000)

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
    ) -> Dict[str, Any]:
        endpoint = "/fapi/v1/order"
        url = BASE_URL + endpoint

        params: Dict[str, Any] = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": self._get_timestamp(),
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)

        logger.debug(f"API Request → POST {endpoint} | Params: { {k: v for k, v in params.items() if k != 'signature'} }")

        try:
            response = self.session.post(url, params=params, timeout=10)
            data = response.json()
            logger.debug(f"API Response → Status: {response.status_code} | Body: {data}")

            if response.status_code != 200:
                error_msg = data.get("msg", "Unknown API error")
                logger.error(f"API Error {data.get('code', '?')}: {error_msg}")
                raise RuntimeError(f"API Error {data.get('code', '?')}: {error_msg}")

            return data

        except requests.exceptions.ConnectionError:
            logger.error("Network failure: Could not connect to Binance Testnet.")
            raise RuntimeError("Network failure: Could not connect to Binance Testnet.")
        except requests.exceptions.Timeout:
            logger.error("Request timed out.")
            raise RuntimeError("Request timed out. Please try again.")
