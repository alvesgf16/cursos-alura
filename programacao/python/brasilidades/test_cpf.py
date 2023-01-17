import pytest
from cpf import Cpf


def test_valid_cpf_is_displayed_with_formatting():
    cpf = Cpf("01234567890")
    assert str(cpf) == "012.345.678-90"


def test_invalid_cpf_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF!"):
        Cpf(15616987913)


def test_cpf_with_length_other_than_11_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        Cpf(1561698791)
