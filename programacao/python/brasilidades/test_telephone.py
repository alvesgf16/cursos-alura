import pytest
from telephone import Telephone


def test_invalid_phone_number_raises_an_error():
    with pytest.raises(ValueError, match="Invalid number!"):
        Telephone("26481234")

