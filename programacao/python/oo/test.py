def create_account(number, holder, balance, limit):
    account = {"number": number, "holder": holder, "balance": balance, "limit": limit}
    return account


def deposit(account, value):
    account["balance"] += value


def withdraw(account, value):
    account["balance"] -= value


def statement(account):
    print(f"Balance: {account['balance']}")
