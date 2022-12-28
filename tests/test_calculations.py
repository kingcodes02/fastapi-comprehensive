import pytest
from app.calculations import *


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(100)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (29, 1, 30),
    (15, 5, 20)
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    print("testing subtract function")
    assert subtract(5, 3) == 2


def test_multiply():
    print("testing multipy function")
    assert multipy(2, 3) == 6


def test_divide():
    print("testing divide function")
    assert divide(6, 2) == 3


def test_bank_set_inital_amount(bank_account):
    assert bank_account.balance == 100


def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 80


def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 120


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
