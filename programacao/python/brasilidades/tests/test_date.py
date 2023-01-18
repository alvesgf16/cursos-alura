from freezegun import freeze_time
from date import Date


@freeze_time("1999-12-05")
def test_month_is_displayed_in_full():
    assert Date().registration_month == "December"


@freeze_time("1994-12-07")
def test_day_of_the_week_is_displayed_in_full():
    assert Date().day_of_the_week == "Wednesday"
