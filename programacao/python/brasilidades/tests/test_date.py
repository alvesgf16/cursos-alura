from freezegun import freeze_time
from date import Date


@freeze_time("1999-12-05")
def test_month_is_displayed_in_full():
    assert Date().registration_month == "December"
