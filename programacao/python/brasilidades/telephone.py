import re


class Telephone:
    def __init__(self, phone_number):
        self.pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        if self.validate(phone_number):
            self.number = phone_number
        else:
            raise ValueError("Invalid number!")

    def __str__(self):
        return self.format()

    def validate(self, phone_number):
        result = re.findall(self.pattern, phone_number)
        if result:
            return True
        else:
            return False

    def format(self):
        result = re.search(self.pattern, self.number)
        return "+{} ({}) {}-{}".format(
            result.group(1),
            result.group(2),
            result.group(3),
            result.group(4)
        )
