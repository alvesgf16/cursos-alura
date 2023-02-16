import unittest

import pytest

from main import Customer, CurrentAccount


class TestMain(unittest.TestCase):
    def setUp(self):
        self.name = "a name"
        self.cpf = "123.456.789-01"
        self.occupation = "student"
        self.customer = Customer(self.name, self.cpf, self.occupation)

    def test_customer_has_a_name_cpf_and_occupation(self):
        assert self.customer.name == self.name
        assert self.customer.cpf == self.cpf
        assert self.customer.occupation == self.occupation

    @pytest.mark.xfail
    def test_customer_has_an_age(self):
        age = 18

        assert self.customer.age == age

    def test_current_account_has_a_customer_agency_and_number(self):
        agency = "1"
        number = "00001"

        account = CurrentAccount(self.customer, agency, number)

        assert account.customer == self.customer
        assert account.agency == agency
        assert account.number == number
