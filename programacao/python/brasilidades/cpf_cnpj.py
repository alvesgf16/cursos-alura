from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, document, document_type):
        document = str(document)
        self.document_type = document_type
        if self.document_type == "cpf":
            if not self.is_cpf_valid(document):
                raise ValueError("Invalid CPF!")
            self.cpf = document

    def __str__(self):
        return self.format_cpf()

    def is_cpf_valid(self, cpf):
        CPF_LENGTH = 11
        if len(cpf) != CPF_LENGTH:
            raise ValueError("Invalid number of digits!")
        return CPF().validate(cpf)

    def format_cpf(self):
        return CPF().mask(self.cpf)
