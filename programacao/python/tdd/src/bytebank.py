from datetime import date


class Employee:
    def __init__(self, name, birth_date, salary):
        self._name = name
        self._birth_date = birth_date
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    def age(self):
        split_birth_date = self._birth_date.split("/")
        birth_year = split_birth_date[-1]
        current_year = date.today().year
        return current_year - int(birth_year)

    def last_name(self):
        full_name = self.name.strip()
        split_name = full_name.split(" ")
        return split_name[-1]

    def decrease_salary(self):
        if self._is_partner():
            decrease = self._salary * 0.1
            self._salary -= decrease

    def _is_partner(self):
        last_names = [
            "Bragança",
            "Windsor",
            "Bourbon",
            "Yamata",
            "Al Saud",
            "Khan",
            "Tudor",
            "Ptolomeu",
        ]
        return self._salary >= 100000 and self.last_name() in last_names

    def calcularte_bonus(self):
        value = self._salary * 0.1
        if value > 1000:
            value = 0
        return value

    def __str__(self):
        return f"Funcionario({self._name}, {self._birth_date}, {self._salary})"
