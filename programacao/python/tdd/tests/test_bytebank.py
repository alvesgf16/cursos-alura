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
