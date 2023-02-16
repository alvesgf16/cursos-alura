import unittest

import pytest

from main import Customer, CurrentAccount


class TestCustomer(unittest.TestCase):
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

class TestCurrentAccount(unittest.TestCase):
    def setUp(self):
        name, cpf, occupation = "a name", "123.456.789-01", "student"
        self.customer = Customer(name, cpf, occupation)
        self.agency = "1"
        self.number = "00001"
        self.account = CurrentAccount(self.customer, self.agency, self.number)

    def test_new_current_account_has_a_customer_agency_and_number(self):
        assert self.account.customer == self.customer
        assert self.account.agency == self.agency
        assert self.account.number == self.number

    def test_new_account_is_initialized_with_a_balance_of_100(self):
        assert self.account.balance == 100

    def test_adding_an_account_increases_the_total_accounts_created(self):
        assert CurrentAccount.total_accounts_created == 1

        name, cpf, occupation = "other name", "183.297.197-07", "developer"
        new_customer = Customer(name, cpf, occupation)
        new_number = "00002"
        CurrentAccount(new_customer, self.agency, new_number)

        assert CurrentAccount.total_accounts_created == 2