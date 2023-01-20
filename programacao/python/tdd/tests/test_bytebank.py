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
