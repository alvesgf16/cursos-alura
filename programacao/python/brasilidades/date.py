from datetime import datetime


class Date:
    def __init__(self):
        self.registration_time = datetime.now()

    def __str__(self):
        return self.format()

    @property
    def registration_month(self):
        months_of_the_year = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        registration_month = self.registration_time.month - 1
        return months_of_the_year[registration_month]

    @property
    def day_of_the_week(self):
        days_of_the_week = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day_of_the_week = self.registration_time.weekday()
        return days_of_the_week[day_of_the_week]

    def format(self):
        return self.registration_time.strftime("%d/%m/%Y %H:%M")
