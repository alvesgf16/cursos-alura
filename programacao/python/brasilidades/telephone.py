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

    def is_valid(self, phone_number):
        return bool(re.findall(self.pattern, phone_number))

    def format(self):
        result = re.search(self.pattern, self.number)
        return "+{} ({}) {}-{}".format(
            result.group(1),
            result.group(2),
            result.group(3),
            result.group(4)
        )
