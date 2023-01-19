import pytest
from requests.exceptions import HTTPError
from unittest.mock import patch
from address import Address
from .mocks.mock_requests_get import mock_requests_get


def test_invalid_cep_raises_an_error():
    with pytest.raises(ValueError, match="Invalid CEP!"):
        Address("264812345")


def test_valid_cep_is_displayed_with_formatting():
    cep = Address("55212648")
    assert "55212-648" == str(cep)


def test_it_is_possible_to_use_a_cep_to_retrieve_address_info():
    cep = Address("49020050")
    with patch("requests.get", side_effect=mock_requests_get):
        assert ("Treze de Julho", "Aracaju", "SE") == cep.zone_info


def test_a_non_existent_cep_raises_an_exception():
    cep = Address("99999999")
    with patch("requests.get", side_effect=mock_requests_get):
        with pytest.raises(HTTPError, match="CEP not found!"):
            cep.zone_info
