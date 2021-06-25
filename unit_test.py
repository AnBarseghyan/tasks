import pytest
import unit2


@pytest.mark.parametrize('balance, interest_rate, payment_rate, months, result',
                         [(42, 0.2, 0.04, 12, 31.38), (484, 0.2, 0.04, 12, 361.61), (122, 0.18, 0.05, 12, 78.82),
                          (305, 0.18, 0.08, 12, 134.07)])
def test_get_credit_card_balance(balance, interest_rate, payment_rate, months, result):
    assert unit2.get_credit_card_balance(balance, interest_rate, payment_rate) == result


@pytest.mark.parametrize('balance, interest_rate, months, result',
                         [(3329, 0.2, 12, 310), (4773, 0.2, 12, 440), (3926, 0.2, 12, 360)])
def test_get_monthly_payment(balance, interest_rate, months, result):
    assert unit2.get_monthly_payment(balance, interest_rate, months) == result


def report():
    print("The Testing process is over")
import atexit
atexit.register(report)


def test_unit2problems():
    assert unit2.get_credit_card_balance(42, 0.2, 0.04) == 31.38
    assert unit2.get_monthly_payment(3329, 0.2) == 310
