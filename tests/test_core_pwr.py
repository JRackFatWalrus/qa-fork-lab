from decimal import Decimal

import pytest

from fixture_calc.core import apply_discount


@pytest.mark.parametrize("price,percent,expected", [
    (Decimal("0.125"), 0, Decimal("0.13")),
    (Decimal("0.135"), 0, Decimal("0.14")),
    (Decimal("0.124"), 0, Decimal("0.12")),
    (Decimal("10"), 0, Decimal("10.00")),
    (Decimal("0.25"), 50, Decimal("0.13")),
    (Decimal("0.27"), 50, Decimal("0.14")),
    (Decimal("10.00"), 10, Decimal("9.00")),
    (Decimal("100.00"), 1, Decimal("99.00")),
    (Decimal("100.00"), 99, Decimal("1.00")),
    (Decimal("100.00"), 100, Decimal("0.00")),
    (Decimal("0"), 50, Decimal("0.00")),
])
def test_apply_discount_values(price, percent, expected):
    assert apply_discount(price, percent) == expected


def test_apply_discount_negative_price():
    with pytest.raises(ValueError, match="price must not be negative") as excinfo:
        apply_discount(Decimal("-0.01"), 10)
    assert "negative" in str(excinfo.value)


def test_apply_discount_percent_below_zero():
    with pytest.raises(ValueError, match="percent must be between 0 and 100"):
        apply_discount(Decimal("10.00"), -1)


def test_apply_discount_percent_above_hundred():
    with pytest.raises(ValueError, match="percent must be between 0 and 100"):
        apply_discount(Decimal("10.00"), 101)
