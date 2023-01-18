import pytest
from cpf_cnpj import create_document


def test_valid_cpf_is_displayed_with_formatting():
    cpf = create_document("01234567890", "cpf")
    assert str(cpf) == "012.345.678-90"


def test_invalid_cpf_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF!"):
        create_document(15616987913, "cpf")


def test_cpf_with_length_other_than_11_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        create_document(1561698791, "cpf")


def test_valid_cnpj_is_displayed_with_formatting():
    cnpj = create_document("05854667000175", "cnpj")
    assert str(cnpj) == "05.854.667/0001-75"


def test_invalid_cnpj_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CNPJ!"):
        create_document(15616987913301, "cnpj")


def test_cnpj_with_length_other_than_14_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        create_document(1561698791, "cnpj")


def test_passing_a_different_document_type_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid document!"):
        create_document(000000000000, "invalid_type")
