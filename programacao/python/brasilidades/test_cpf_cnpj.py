import pytest
from cpf_cnpj import CpfCnpj


def test_valid_cpf_is_displayed_with_formatting():
    cpf = CpfCnpj("01234567890")
    assert str(cpf) == "012.345.678-90"


def test_invalid_cpf_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF!"):
        CpfCnpj(15616987913)


def test_cpf_with_length_other_than_11_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        CpfCnpj(1561698791)
