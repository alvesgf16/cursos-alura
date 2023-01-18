from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        if not self.is_valid(document):
            raise ValueError("Invalid CPF!")
        self.cpf = document

    def __str__(self):
        return self.format()

    def is_valid(self, cpf):
        return CPF().validate(cpf)

    def format(self):
        return CPF().mask(self.cpf)
