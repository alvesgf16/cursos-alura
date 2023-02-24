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

        self.__customer = a_customer
        self.__set__agency(an_agency)
        self.__number = a_number
        CurrentAccount.total_accounts_created += 1
        CurrentAccount.operation_fee = (
            30 / CurrentAccount.total_accounts_created
        )

    @property
    def balance(self):
        return self.__balance

    @property
    def customer(self):
        return self.__customer

    @property
    def agency(self):
        return self.__agency

    def __set__agency(self, an_agency):
        if not isinstance(an_agency, int):
            raise ValueError("Attribute must be an integer")

        self.__agency = an_agency

    @property
    def number(self):
        return self.__number

    def transfer(self, an_amount, an_account):
        self.withdraw(an_amount)
        an_account.deposit(an_amount)

    def withdraw(self, an_amount):
        self.__balance -= an_amount

    def deposit(self, an_amount):
        self.__balance += an_amount
