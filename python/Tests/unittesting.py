import unittest
from bankaccount import BankAccount


class TestClass(unittest.TestCase):

    def setUp(self):
        self.bank = BankAccount(123456)

    # test if deposit works
    def test_deposit(self):
        self.bank.deposit(20)
        self.assertEqual(self.bank.balance, 20, "Deposit doesnt work!")

    def test_withdraw(self):
        self.bank.deposit(10)
        withdrawn = self.bank.withdraw(12)
        self.assertTrue(withdrawn, "cant withdraw!")



