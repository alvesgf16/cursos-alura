from main import Customer


def test_customer_has_a_name_cpf_and_occupation():
    name = "a name"
    cpf = "123.456.789-01"
    occupation = "student"
    
    customer = Customer(name, cpf, occupation)

    assert customer.name == name
    assert customer.cpf == cpf
    assert customer.occupation == occupation