"""Small, pure functions. `add` is tested; `apply_discount` deliberately has no test."""

from decimal import ROUND_HALF_UP, Decimal


def add(a: int, b: int) -> int:
    return a + b


def apply_discount(price: Decimal, percent: int) -> Decimal:
    """Return ``price`` reduced by ``percent`` per cent, rounded to cents.

    ``percent`` must be between 0 and 100 inclusive; anything else raises ``ValueError``.
    A negative price raises ``ValueError``.
    """
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    if price < 0:
        raise ValueError("price must not be negative")
    discounted = price * (Decimal(100) - Decimal(percent)) / Decimal(100)
    return discounted.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
