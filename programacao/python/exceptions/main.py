class Customer:
    def __init__(self, name, cpf, occupation):
        self.__name = name
        self.__cpf = cpf
        self.__occupation = occupation

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
    def __init__(self, customer, agency, number):
        self.__balance = 100
        self.__customer = customer
        self.__agency = agency
        self.__number = number
    
    @property
    def balance(self):
        return self.__balance

    @property
    def customer(self):
        return self.__customer

    @property
    def agency(self):
        return self.__agency

    @property
    def number(self):
        return self.__number    