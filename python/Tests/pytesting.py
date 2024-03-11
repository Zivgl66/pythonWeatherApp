"""
This Test module uses pytest to test the BankAccount Class
every function checks a different aspect of the class (methods, initializations)
"""

import pytest
from bankaccount import BankAccount


@pytest.fixture()
def bank():
    return BankAccount(123456)


# test to check initialization of bank object, balance
def test_default_initial_amount(bank):
    assert bank.balance == 0


# test to check initialization of bank object, id
def test_id_initialization(bank):
    assert bank.bank_id == 123456


# test to check bank class method, deposit
def test_deposit_amount(bank):
    deposit_return = bank.deposit(20)
    assert deposit_return


# test to check bank class method, withdraw a good amount
def test_withdraw_true(bank):
    bank.deposit(12)
    withdraw_true = bank.withdraw(10)
    assert withdraw_true


# test to check bank class method, withdraw more than the balance
def test_withdraw_amount_not_enough(bank):
    bank.deposit(10)
    withdraw_return = bank.withdraw(5)
    assert withdraw_return, "Not enough money, should be false"



