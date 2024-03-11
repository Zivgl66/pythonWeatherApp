"""
This is the BankAccount module.

The Bank account module is used for testing

>>> b = BankAccount(12345)
>>> b.bank_id
12345
"""


class BankAccount:
    def __init__(self, bank_id):
        self.bank_id = bank_id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
