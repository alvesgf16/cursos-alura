from validate_docbr import CNPJ


class Cnpj:
    def __init__(self, document):
        if not self.is_valid(document):
            raise ValueError("Invalid CNPJ!")
        self.cnpj = document

    def __str__(self):
        return self.format()

    def is_valid(self, cnpj):
        CNPJ_LENGTH = 14
        if len(cnpj) != CNPJ_LENGTH:
            raise ValueError("Invalid number of digits!")
        return CNPJ().validate(cnpj)

    def format(self):
        return CNPJ().mask(self.cnpj)
