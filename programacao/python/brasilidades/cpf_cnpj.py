from cpf import Cpf
from cnpj import Cnpj


def create_document(document, document_type):
    document = str(document)
    if document_type == "cpf":
        return Cpf(document)
    elif document_type == "cnpj":
        return Cnpj(document)
    else:
        raise ValueError("Invalid document!")
