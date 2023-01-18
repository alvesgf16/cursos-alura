import pytest
from cpf_cnpj import create_document


def test_valid_cpf_is_displayed_with_formatting():
    cpf = create_document("01234567890")
    assert str(cpf) == "012.345.678-90"


def test_invalid_cpf_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF!"):
        create_document(15616987913)


def test_valid_cnpj_is_displayed_with_formatting():
    cnpj = create_document("05854667000175")
    assert str(cnpj) == "05.854.667/0001-75"


def test_invalid_cnpj_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CNPJ!"):
        create_document(15616987913301)


def test_document_with_invalid_length_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        create_document(1561698791)
