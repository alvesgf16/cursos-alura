def create_account(number, holder, balance, limit):
    return {"number": number, "holder": holder, "balance": balance, "limit": limit}


def deposit(account, value):
    account["balance"] += value


def withdraw(account, value):
    account["balance"] -= value


def statement(account):
    print(f"Balance: {account['balance']}")
