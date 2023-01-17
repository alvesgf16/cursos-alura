import pytest
from cpf import Cpf


def test_cpf_with_length_other_than_11_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF"):
        Cpf(1561698791)
