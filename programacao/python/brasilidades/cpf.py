class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.is_cpf_valid(document):
            self.cpf = document
        else:
            raise ValueError("Invalid CPF!")

    def is_cpf_valid(self, document):
        if len(document) == 11:
            return True
        else:
            return False

