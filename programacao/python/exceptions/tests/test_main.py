import unittest

import pytest

from main import Customer, CurrentAccount


class TestMain(unittest.TestCase):
    def setUp(self):
        self.name = "a name"
        self.cpf = "123.456.789-01"
        self.occupation = "student"
        self.customer = Customer(self.name, self.cpf, self.occupation)

    def test_new_customer_has_a_name_cpf_and_occupation(self):
        assert self.customer.name == self.name
        assert self.customer.cpf == self.cpf
        assert self.customer.occupation == self.occupation

    @pytest.mark.xfail
    def test_new_customer_has_an_age(self):
        age = 18

        assert self.customer.age == age

    def test_new_current_account_has_a_customer_agency_and_number(self):
        agency = "1"
        number = "00001"

        account = CurrentAccount(self.customer, agency, number)

        assert account.customer == self.customer
        assert account.agency == agency
        assert account.number == number

    def test_new_account_is_initialized_with_a_balance_of_100(self):
        agency = "1"
        number = "00001"

        account = CurrentAccount(self.customer, agency, number)

        assert account.balance == 100

    def test_adding_an_account_increases_the_total_accounts_created(self):
        agency = "1"
        number = "00001"

        CurrentAccount(self.customer, agency, number)

        assert CurrentAccount.total_accounts_created == 1
