import pytest
from mortgage import monthly_payment, total_payment, overpayment


def test_monthly_payment_basic():
    # 1 000 000 под 12% на 1 год — примерно 88 848.79
    result = monthly_payment(1_000_000, 12, 1)
    assert result == pytest.approx(88848.79, rel=0.01)


def test_monthly_payment_longer_term():
    # Чем дольше срок, тем меньше ежемесячный платёж
    short = monthly_payment(1_000_000, 12, 1)
    long = monthly_payment(1_000_000, 12, 10)
    assert long < short


def test_total_payment_exceeds_principal():
    # Всегда переплачиваем больше, чем взяли
    assert total_payment(1_000_000, 12, 5) > 1_000_000


def test_overpayment_positive():
    assert overpayment(1_000_000, 12, 5) > 0


def test_invalid_input_raises():
    with pytest.raises(ValueError):
        monthly_payment(-100, 12, 1)
    with pytest.raises(ValueError):
        monthly_payment(100, 0, 1)
    with pytest.raises(ValueError):
        monthly_payment(100, 12, -1)
