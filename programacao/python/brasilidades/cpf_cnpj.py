from cpf import Cpf
from cnpj import Cnpj


def create_document(document):
    document = str(document)
    if len(document) == 11:
        return Cpf(document)
    elif len(document) == 14:
        return Cnpj(document)
    else:
        raise ValueError("Invalid number of digits!")
