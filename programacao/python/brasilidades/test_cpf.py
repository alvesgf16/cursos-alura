import pytest
from cpf import Cpf


def test_valid_cpf_is_displayed_with_formatting():
    cpf = Cpf(15616987913)
    assert str(cpf) == "156.169.879-13"


def test_cpf_with_length_other_than_11_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF"):
        Cpf(1561698791)
