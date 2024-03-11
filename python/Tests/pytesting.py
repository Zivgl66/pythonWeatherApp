import pytest
from bankaccount import BankAccount

bank = BankAccount(123456)


def test_default_initial_amount():
    assert bank.balance == 0


def test_id_initialization():
    assert bank.bank_id == 123456


def test_deposit_amount():
    deposit_return = bank.deposit(20)
    assert deposit_return


def test_withdraw_true():
    withdraw_true = bank.withdraw(10)
    assert withdraw_true


def test_withdraw_amount_not_enough():
    withdraw_return = bank.withdraw(25)
    assert withdraw_return, "Not enough money, should be false"



