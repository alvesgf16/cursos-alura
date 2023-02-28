import unittest

import pytest

from bank import Customer, CurrentAccount
from exceptions import InsufficientFundsError


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
        self.agency = 1
        self.number = 1
        self.account = CurrentAccount(self.customer, self.agency, self.number)

    def tearDown(self):
        CurrentAccount.total_accounts_created = 0

    def test_new_current_account_has_a_customer_agency_and_number(self):
        assert self.account.customer == self.customer
        assert self.account.agency == self.agency
        assert self.account.number == self.number

    def test_new_account_is_initialized_with_a_balance_of_100(self):
        assert self.account.balance == 100

    def test_adding_an_account_increases_the_total_accounts_created(self):
        assert CurrentAccount.total_accounts_created == 1

        self.given_a_second_account()

        assert CurrentAccount.total_accounts_created == 2

    def test_withdraw_decreases_balance(self):
        withdrawal_amount = 10
        balance_after_withdrawal = 90

        self.account.withdraw(withdrawal_amount)

        assert self.account.balance == balance_after_withdrawal

    def test_withdrawing_more_than_the_available_funds_raises_an_error(self):
        withdrawal_amount = 150

        with pytest.raises(InsufficientFundsError):
            self.account.withdraw(withdrawal_amount)

    def test_deposit_increases_balance(self):
        deposit_amount = 10
        balance_after_deposit = 110

        self.account.deposit(deposit_amount)

        assert self.account.balance == balance_after_deposit

    def test_transfer_decreases_a_balance_and_increases_another(self):
        transfer_amount = 10
        destination_account = self.given_a_second_account()
        origin_balance_after_transfer = 90
        destination_balance_after_transfer = 110

        self.account.transfer(transfer_amount, destination_account)

        assert self.account.balance == origin_balance_after_transfer
        assert (
            destination_account.balance == destination_balance_after_transfer
        )

    def test_adding_an_account_decreases_the_operation_fee(self):
        assert CurrentAccount.operation_fee == 30

        self.given_a_second_account()

        assert CurrentAccount.operation_fee == 15

    def test_agency_is_an_integer(self):
        with pytest.raises(TypeError, match="Attribute must be an integer"):
            agency_str = "1"
            CurrentAccount(self.customer, agency_str, self.number)

    def test_agency_is_positive(self):
        with pytest.raises(
            ValueError, match="Attribute must be greater than zero"
        ):
            agency_non_positive = 0
            CurrentAccount(self.customer, agency_non_positive, self.number)

    def test_number_is_an_integer(self):
        with pytest.raises(TypeError, match="Attribute must be an integer"):
            number_str = "00001"
            CurrentAccount(self.customer, self.agency, number_str)

    def test_number_is_positive(self):
        with pytest.raises(
            ValueError, match="Attribute must be greater than zero"
        ):
            number_non_positive = 0
            CurrentAccount(self.customer, self.agency, number_non_positive)

    def given_a_second_account(self):
        name, cpf, occupation = "other name", "183.297.197-07", "developer"
        new_customer = Customer(name, cpf, occupation)
        new_number = 2
        return CurrentAccount(new_customer, self.agency, new_number)
