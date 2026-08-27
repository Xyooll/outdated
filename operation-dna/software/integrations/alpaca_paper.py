"""Explicitly gated Alpaca paper-trading adapter."""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

import requests

PAPER_BASE_URL = "https://paper-api.alpaca.markets"

@dataclass(frozen=True)
class PaperAccount:
    id: str
    status: str
    equity: float
    buying_power: float
    trading_blocked: bool

class AlpacaPaperAdapter:
    name = "alpaca-paper"
    side_effects = True

    def __init__(self, api_key: str | None = None, api_secret: str | None = None,
                 base_url: str = PAPER_BASE_URL, session: requests.Session | None = None):
        if base_url.rstrip("/") != PAPER_BASE_URL:
            raise ValueError("paper adapter refuses non-paper Alpaca endpoints")
        self.api_key = api_key or os.getenv("APCA_API_KEY_ID")
        self.api_secret = api_secret or os.getenv("APCA_API_SECRET_KEY")
        if not self.api_key or not self.api_secret:
            raise RuntimeError("APCA_API_KEY_ID and APCA_API_SECRET_KEY are required")
        self.base_url = PAPER_BASE_URL
        self.session = session or requests.Session()

    @property
    def headers(self) -> dict[str, str]:
        return {"APCA-API-KEY-ID": self.api_key, "APCA-API-SECRET-KEY": self.api_secret,
                "Content-Type": "application/json"}

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        response = self.session.request(method, f"{self.base_url}{path}",
                                        headers=self.headers, timeout=15, **kwargs)
        response.raise_for_status()
        return response.json() if response.content else {}

    def account(self) -> PaperAccount:
        data = self._request("GET", "/v2/account")
        return PaperAccount(str(data["id"]), str(data["status"]), float(data["equity"]),
                            float(data["buying_power"]), bool(data.get("trading_blocked", False)))

    def get_order(self, order_id: str) -> dict[str, Any]:
        return self._request("GET", f"/v2/orders/{order_id}")

    def get_orders(self, status: str = "all", limit: int = 100) -> list[dict[str, Any]]:
        return self._request("GET", "/v2/orders", params={"status": status, "limit": limit})

    def get_positions(self) -> list[dict[str, Any]]:
        return self._request("GET", "/v2/positions")

    def submit_market_order(self, symbol: str, qty: float, side: str,
                            client_order_id: str | None = None) -> dict[str, Any]:
        if not symbol or "/" in symbol: raise ValueError("paper stock order symbol must be a stock ticker, e.g. AAPL")
        if qty <= 0: raise ValueError("qty must be > 0")
        if side not in {"buy", "sell"}: raise ValueError("side must be buy or sell")
        payload = {"symbol": symbol.upper(), "qty": str(qty), "side": side,
                   "type": "market", "time_in_force": "day"}
        if client_order_id: payload["client_order_id"] = client_order_id
        return self._request("POST", "/v2/orders", json=payload)

    def cancel_order(self, order_id: str) -> Any:
        return self._request("DELETE", f"/v2/orders/{order_id}")

    def cancel_all_orders(self) -> Any:
        return self._request("DELETE", "/v2/orders")
