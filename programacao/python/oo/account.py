class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def statement(self):
        print(f"Balance: {self.__balance} // Holder: {self.__holder}")

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)

