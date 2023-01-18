import re


class Telephone:
    def __init__(self, phone_number):
        self.pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        if self.is_valid(phone_number):
            self.number = phone_number
        else:
            raise ValueError("Invalid number!")

    def __str__(self):
        return self.format()

    @property
    def number_parts(self):
        return re.search(self.pattern, self.number).groups()

    def is_valid(self, phone_number):
        return bool(re.findall(self.pattern, phone_number))

    def format(self):
        country_code, area_code, prefix, line_number = self.number_parts
        result = ""
        if country_code is not None:
            result += f"+{country_code} "
        result += f"({area_code}) {prefix}-{line_number}"
        return result
