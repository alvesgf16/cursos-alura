import pytest
from cep_access import AddressSearch


def test_invalid_cep_raises_an_error():
    with pytest.raises(ValueError, match="Invalid CEP!"):
        AddressSearch("264812345")


def test_valid_cep_is_displayed_with_formatting():
    cep = AddressSearch("55212648")
    assert "55212-648" == str(cep)


def test_it_is_possible_to_use_a_cep_to_retrieve_address_info():
    cep = AddressSearch("49020050")
    assert ("Treze de Julho", "Aracaju", "SE") == cep.access_via_cep()
