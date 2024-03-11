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

