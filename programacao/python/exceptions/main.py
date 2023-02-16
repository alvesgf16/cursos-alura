class Customer:
    def __init__(self, name, cpf, occupation):
        self.name = name
        self.cpf = cpf
        self.occupation = occupation


class CurrentAccount:
    def __init__(self, customer, agency, number):
        self.customer = customer
        self.agency = agency
        self.number = number
        