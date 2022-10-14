class Account:
    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def deposit(self, amount):
        self.__balance += amount

    def __can_withdraw(self, withdrawal_amount):
        available_credit = self.__balance + self.__limit
        return withdrawal_amount <= available_credit

    def withdraw(self, amount):
        if self.__can_withdraw(amount):
            self.__balance -= amount
        else:
            print(f"The amount {amount} is over the limit")

    def statement(self):
        print(f"Balance: {self.__balance} // Holder: {self.__holder}")

    def transfer(self, amount, destination):
        self.withdraw(amount)
        destination.deposit(amount)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
