from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.is_cpf_valid(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF!")

    def __str__(self):
        return self.format_cpf()

    def is_cpf_valid(self, cpf):
        if len(cpf) != 11:
            raise ValueError("Invalid number of digits!")
        else:
            validator = CPF()
            return validator.validate(cpf)

    def format_cpf(self):
        mask = CPF()
        return mask.mask(self.cpf)
