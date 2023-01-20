import re


class Telephone:
    def __init__(self, phone_number):
        self.pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        if self.is_valid(phone_number):
            self.number = phone_number
        else:
            raise ValueError("Invalid number!")

    def __str__(self):
        result = self.start_with_country_code_if_exists()
        result += self.format()
        return result

    @property
    def number_parts(self):
        return re.search(self.pattern, self.number).groups()

    def is_valid(self, phone_number):
        return bool(re.findall(self.pattern, phone_number))

    def start_with_country_code_if_exists(self):
        country_code = self.number_parts[0]
        return f"+{country_code} " if country_code is not None else ""

    def format(self):
        area_code, prefix, line_number = self.number_parts[1:]
        return f"({area_code}) {prefix}-{line_number}"