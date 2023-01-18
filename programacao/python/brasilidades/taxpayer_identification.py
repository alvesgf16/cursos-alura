from cpf import Cpf
from cnpj import Cnpj


def create_taxpayer_identification(id_number):
    id_number = str(id_number)
    if len(id_number) == 11:
        return Cpf(id_number)
    elif len(id_number) == 14:
        return Cnpj(id_number)
    else:
        raise ValueError("Invalid number of digits!")
