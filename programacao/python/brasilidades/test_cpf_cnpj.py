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
        CpfCnpj(1561698791, "cpf")


def test_invalid_cnpj_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CNPJ!"):
        CpfCnpj(15616987913301, "cnpj")


def test_cnpj_with_length_other_than_14_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        CpfCnpj(1561698791, "cnpj")
