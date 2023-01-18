from cpf import Cpf
from cnpj import Cnpj


def create_taxpayer_identification(id_number):
    CPF_LENGTH = 11
    CNPJ_LENGTH = 14

    id_number = str(id_number)
    if len(id_number) == CPF_LENGTH:
        return Cpf(id_number)
    elif len(id_number) == CNPJ_LENGTH:
        return Cnpj(id_number)
    else:
        raise ValueError("Invalid number of digits!")
