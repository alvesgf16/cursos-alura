from main import Customer, CurrentAccount
import pytest


def test_customer_has_a_name_cpf_and_occupation():
    name = "a name"
    cpf = "123.456.789-01"
    occupation = "student"
    
    customer = Customer(name, cpf, occupation)

    assert customer.name == name
    assert customer.cpf == cpf
    assert customer.occupation == occupation


@pytest.mark.xfail
def test_customer_has_an_age():
    name = "a name"
    cpf = "123.456.789-01"
    occupation = "student"
    age = 18

    customer = Customer(name, cpf, occupation)

    assert customer.age == age


def test_current_account_class_exists():
    CurrentAccount()
