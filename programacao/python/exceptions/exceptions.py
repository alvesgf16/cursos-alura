class InsufficientFundsError(Exception):
    def __init__(self, a_message="", a_balance=None, an_amount=None):
        self.balance = a_balance
        self.amount = an_amount
        super(InsufficientFundsError, self).__init__(a_message or self.msg)

    @property
    def msg(self):
        return (
            "Insufficient balance to carry out the transaction\n" +
            f"Current balance: {self.balance} - " +
            f"Amount to be withdrawn: {self.amount}"
        )
