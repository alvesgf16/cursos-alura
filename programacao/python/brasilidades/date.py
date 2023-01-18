from datetime import datetime


class Date:
    def __init__(self):
        self.registration_time = datetime.now()

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

