from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        document = str(document)
        if not self.is_cpf_valid(document):
            raise ValueError("Invalid CPF!")
        self.cpf = document

    def __str__(self):
        return self.format_cpf()

    def is_cpf_valid(self, cpf):
        if len(cpf) != 11:
            raise ValueError("Invalid number of digits!")
        return CPF().validate(cpf)

    def format_cpf(self):
        return CPF().mask(self.cpf)
