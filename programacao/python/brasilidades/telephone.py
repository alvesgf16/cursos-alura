import re


class Telephone:
    def __init__(self, phone_number):
        if self.validate(phone_number):
            self.number = phone_number
        else:
            raise ValueError("Invalid number!")

    def validate(self, phone_number):
        pattern = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        result = re.findall(pattern, phone_number)
        if result:
            return True
        else:
            return False
