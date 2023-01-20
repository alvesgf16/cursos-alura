import pytest
from pytest import mark
from src.bytebank import Employee


class TestClass:
    def test_when_age_receives_13_03_2000_must_return_23(self):
        # Given / Arrange
        input_date = "13/03/2000"
        expected = 23

        test_employee = Employee("Test", input_date, 1111)

        # When / Act
        result = test_employee.age()

        # Then / Assert
        assert result == expected

    def test_when_last_name_receives_Lucas_Carvalho_must_return_Carvalho(self):
        # Given / Arrange
        input_name = " Lucas Carvalho "
        expected = "Carvalho"

        lucas = Employee(input_name, "11/11/2000", 1111)

        # When / Act
        result = lucas.last_name()

        # Then / Assert
        assert result == expected

    def test_when_decrease_salary_receives_100000_must_return_90000(self):
        # Given / Arrange
        input_salary = 100000
        input_name = "Paulo Bragança"
        expected = 90000

        test_employee = Employee(input_name, "11/11/2000", input_salary)

        # When / Act
        test_employee.decrease_salary()
        result = test_employee.salary

        # Then / Assert
        assert result == expected

    @mark.calculate_bonus
    def test_when_calculate_bonus_receives_1000_must_return_100(self):
        # Given / Arrange
        input_salary = 1000
        expected = 100

        test_employee = Employee("Test", "11/11/2000", input_salary)

        # When / Act
        result = test_employee.calculate_bonus()

        # Then / Assert
        assert result == expected

    @mark.calculate_bonus
    def test_when_calculate_bonus_receives_10000000_must_raise_exception(self):
        with pytest.raises(ValueError):
            # Given / Arrange
            input_salary = 10000000

            test_employee = Employee("Test", "11/11/2000", input_salary)

            # When / Act
            result = test_employee.calculate_bonus()

            # Then / Assert
            assert result
