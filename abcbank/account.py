from abcbank.transaction import Transaction
from abcbank.customer import Customer


CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []

    def deposit(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(amount))

    def withdraw(self, amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        else:
            self.transactions.append(Transaction(-amount))

    def transfer(self,initial_account,final_account,amount):
        if (amount <= 0):
            raise ValueError("amount must be greater than zero")
        elif Customer.numAccs()<=1:
            raise ValueError("You must have at least 2 accounts")
        else:
            self.accountType=initial_account
            self.withdraw(amount)
            self.accountType=final_account
            self.deposit(amount)

    def interestEarned(self):
        amount = self.sumTransactions()
        if self.accountType == SAVINGS:
            if (amount <= 1000):
                return amount * 0.001
            else:
                return 1 + (amount - 1000) * 0.002
        if self.accountType == MAXI_SAVINGS:
            if (amount <= 1000):
                return amount * 0.02
            elif (amount <= 2000):
                return 20 + (amount - 1000) * 0.05
            else:
                return 70 + (amount - 2000) * 0.1
        else:
            return amount * 0.001

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
