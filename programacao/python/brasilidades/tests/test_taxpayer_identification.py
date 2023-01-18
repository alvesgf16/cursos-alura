import pytest
from taxpayer_identification import create_taxpayer_identification


def test_valid_cpf_is_displayed_with_formatting():
    cpf = create_taxpayer_identification("01234567890")
    assert "012.345.678-90" == str(cpf)


def test_invalid_cpf_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CPF!"):
        create_taxpayer_identification(15616987913)


def test_valid_cnpj_is_displayed_with_formatting():
    cnpj = create_taxpayer_identification("05854667000175")
    assert "05.854.667/0001-75" == str(cnpj)


def test_invalid_cnpj_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid CNPJ!"):
        create_taxpayer_identification(15616987913301)


def test_document_with_invalid_length_raises_an_exception():
    with pytest.raises(ValueError, match="Invalid number of digits"):
        create_taxpayer_identification(1561698791)
