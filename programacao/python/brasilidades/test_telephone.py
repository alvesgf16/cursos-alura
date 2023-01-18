import pytest
from telephone import Telephone


def test_invalid_phone_number_raises_an_error():
    with pytest.raises(ValueError, match="Invalid number!"):
        Telephone("26481234")


def test_valid_phone_number_is_displayed_with_formatting():
    phone = Telephone("552126481234")
    assert str(phone) == "+55 (21) 2648-1234"
