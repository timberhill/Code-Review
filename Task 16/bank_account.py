
class BasicBankAccount(object):
    '''
    Basic bank account.
    Can withdraw, deposit, holds current balance.
    Does not validate the amounts, can go negative.
    '''
    def __init__(self, initial_balance=0):
        # initialise the object
        # this function is called when you create the object by running:
        # account = BasicBankAccount(100)
        self.balance = initial_balance
    

    def deposit(self, amount):
        '''
        Deposit some amount to current balance
        '''
        self.balance += amount
    

    def withdraw(self, amount):
        '''
        Withdraw some amount from current balance
        '''
        self.balance -= amount



class BetterBankAccount(BasicBankAccount):
    '''
    Basic bank account than the BasicBankAccount.
    Can withdraw, deposit, holds current balance.
    Does not validate the amounts, can go negative.
    '''
    def __init__(self, initial_balance=0):
        # run the init function from BasicBankAccount to set initial balance
        # Can run functions from BasicBankAccount in a similar manner
        BasicBankAccount.__init__(self, initial_balance)
        self.transactions = []
    

    def deposit(self, amount):
        '''
        Deposit some amount to current balance.
        Must be positive.
        '''
        if amount < 0:
            print("Cannot deposit a negative amount.")
            return
        else:
            BasicBankAccount.deposit(self, amount)
            self.transactions.append(amount)


    def withdraw(self, amount):
        '''
        Withdraw some amount from current balance.
        Must be positive, must not exceed current balance.
        '''
        if amount < 0:
            print("Cannot withdraw a negative amount.")
            return
        elif amount > self.balance:
            print("Current balance exceeded. You balance is {0:.2f}".format(self.balance))
            return
        else:
            BasicBankAccount.withdraw(self, amount)
            self.transactions.append(-amount)
    

    def history(self, n=5):
        '''
        Print last N entries in the transaction history.
        '''
        output = ""
        temp_balance = self.balance
        indices = list(range(len(self.transactions)))
        for i, x in zip(reversed(indices[-n:]), reversed(self.transactions[-n:])):
            if x < 0:
                output += "#{} Withdrawn {}. Account balance: {}\n".format(i, abs(x), temp_balance)
            else:
                output += "#{} Deposited {}. Account balance: {}\n".format(i, abs(x), temp_balance)

            temp_balance -= x
        
        if n < len(self.transactions):
            output += "...\n"

        print("Last {} transactions:\n{}".format(n, output))