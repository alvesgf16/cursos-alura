class Account:
    def __init__(self, number, holder, balance, limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def statement(self):
        print(f"Balance: {self.balance} // Holder: {self.holder}")
