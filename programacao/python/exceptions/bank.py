from exceptions import InsufficientFundsError


class Customer:
    def __init__(self, a_name, a_cpf, an_occupation):
        self.__name = a_name
        self.__cpf = a_cpf
        self.__occupation = an_occupation

    @property
    def name(self):
        return self.__name

    @property
    def cpf(self):
        return self.__cpf

    @property
    def occupation(self):
        return self.__occupation


class CurrentAccount:
    total_accounts_created = 0
    operation_fee = None

    def __init__(self, a_customer, an_agency, a_number):
        self.__balance = 100
        self.__agency = 0
        self.__number = 0

        self.__customer = a_customer
        self.__set_agency(an_agency)
        self.__set_number(a_number)
        CurrentAccount.total_accounts_created += 1
        CurrentAccount.operation_fee = (
            30 / CurrentAccount.total_accounts_created
        )

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, a_balance):
        self.__validate_value_is_an_integer(a_balance)
        self.__balance = a_balance

    @property
    def customer(self):
        return self.__customer

    @property
    def agency(self):
        return self.__agency

    def __set_agency(self, an_agency):
        self.__validate_value_is_a_positive_integer(an_agency)
        self.__agency = an_agency

    @property
    def number(self):
        return self.__number

    def __set_number(self, a_number):
        self.__validate_value_is_a_positive_integer(a_number)
        self.__number = a_number

    def __validate_value_is_a_positive_integer(self, a_value):
        self.__validate_value_is_an_integer(a_value)
        self.__validate_value_is_positive(a_value)

    def __validate_value_is_an_integer(self, a_value):
        if not isinstance(a_value, int):
            raise TypeError(f"Attribute must be an integer: {repr(a_value)}")

    def __validate_value_is_positive(self, a_value):
        if a_value <= 0:
            raise ValueError(f"Attribute must be greater than zero: {a_value}")

    def transfer(self, an_amount, an_account):
        self.withdraw(an_amount)
        an_account.deposit(an_amount)

    def withdraw(self, an_amount):
        if self.balance < an_amount:
            raise InsufficientFundsError(
                a_balance=self.balance, an_amount=an_amount
            )
        self.balance -= an_amount

    def deposit(self, an_amount):
        self.balance += an_amount
