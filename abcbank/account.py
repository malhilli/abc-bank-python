from abcbank.transaction import Transaction
from abcbank.customer import Customer
from date_provider import DateProvider

CHECKING = 0
SAVINGS = 1
MAXI_SAVINGS = 2


class Account:
    def __init__(self, accountType):
        self.accountType = accountType
        self.transactions = []
        self.logintimes= []

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
        #This is a false date for testing. A real account would already have recorded the previous transactions
        t=date('2015','11','09')
        self.logintimes.append(t)

        currentTime=DateProvider()
        if self.logintimes is empty:
            return amount*0
        else:
            instance=len(self.logintimes)
            lasLogin=self.logintimes[instance]
            diff=currentTime-lasLogin
            if self.accountType == SAVINGS:
                if (amount <= 1000):
                    return amount * 0.001*diff.days
                else:
                    return 1 + (amount - 1000) * 0.002*diff.days
            if self.accountType == MAXI_SAVINGS:
                if diff.day >=10:
                    return amount * 0.05*diff.days
                else:
                    return amount * 0.001*diff.days
            else:
                return amount * 0.001*diff.days

    def sumTransactions(self, checkAllTransactions=True):
        return sum([t.amount for t in self.transactions])
