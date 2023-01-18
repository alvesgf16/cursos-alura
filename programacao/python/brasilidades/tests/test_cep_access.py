import pytest
from cep_access import AddressSearch


def test_invalid_cep_raises_an_error():
    with pytest.raises(ValueError, match="Invalid CEP!"):
        AddressSearch("264812345")
