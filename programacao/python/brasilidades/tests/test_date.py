from freezegun import freeze_time
from datetime import timedelta
from date import Date


@freeze_time("2023-01-15 23:00:00")
def test_date_is_displayed_with_correct_formatting():
    date = Date()
    assert str(date) == "15/01/2023 23:00"


@freeze_time("1999-12-05")
def test_month_is_displayed_in_full():
    assert Date().registration_month == "December"


@freeze_time("1994-12-07")
def test_day_of_the_week_is_displayed_in_full():
    assert Date().day_of_the_week == "Wednesday"


@freeze_time("1996-07-04 11:00:00", auto_tick_seconds=604800)
def test_time_registration_returns_how_long_a_user_has_been_registered():
    date = Date()
    assert date.time_registered() == timedelta(weeks=1)
