import sys

from bank import Customer, CurrentAccount


accounts = []
while True:
    try:
        name = input("Customer name: ")
        agency = input("Agency number: ")
        number = input("Current account number: ")
        customer = Customer(name, None, None)
        current_account = CurrentAccount(customer, agency, number)
        accounts.append(current_account)
    except KeyboardInterrupt:
        print(f"\n\n{len(accounts)} accounts created")
        sys.exit()
