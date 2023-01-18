from datetime import datetime


class Date:
    def __init__(self):
        self.time_of_registration = datetime.now()

    def __str__(self):
        return self.time_of_registration.strftime("%d/%m/%Y %H:%M")

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
        registration_month = self.time_of_registration.month - 1
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
        day_of_the_week = self.time_of_registration.weekday()
        return days_of_the_week[day_of_the_week]

    def time_registered(self):
        return datetime.now() - self.time_of_registration
