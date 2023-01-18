from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, id_number):
        if not self.is_valid(id_number):
            raise ValueError("Invalid CNPJ!")
        self.id_number = id_number

    def __str__(self):
        return self.format()

    def is_valid(self, id_number):
        return CNPJ().validate(id_number)

    def format(self):
        return CNPJ().mask(self.id_number)
