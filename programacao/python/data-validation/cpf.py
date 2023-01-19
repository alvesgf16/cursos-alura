from validate_docbr import CPF


class Cpf:
    def __init__(self, id_number):
        if not self.is_valid(id_number):
            raise ValueError("Invalid CPF!")
        self.id_number = id_number

    def __str__(self):
        return CPF().mask(self.id_number)

    def is_valid(self, id_number):
        return CPF().validate(id_number)
