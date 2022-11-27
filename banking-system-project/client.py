from account import Account


class Client(object):
    """
    This is the class that represents the client and holds all the accounts created by the user. In addition, this class inherits functionality from the account class.

    Methods
    -------
    - addAccount:add created account to the bank account list.
    - findAccount: this method checks the user's list of accounts to see if the given account number exists.
    - deposit: deposit an amount into a desired account.
    - withdraw: withdraw an amount from a desired account.
    - transfer: transfer an amount from one account to another.
    - checkBalance: check the balance of an account.
    - getNextAccountNumber: create a new bank account number different from the last account created.

    Attributes
    ----------
    accountNumber : int
        Bank account number that will always start with 1000.

    """

    accountNumber = 1000

    def __init__(self):
        """Initial Constructor.    

        Parameters
        ----------
        __accounts : list
            List of bank accounts created by the user.
        """
        self.__accounts = []  # save all account cread by user

    def addAccount(self, account):
        """Add created account to the bank account list.

        Parameters
        ----------
        account : account
            Object account that can be a checking or savings account.
        """
        self.__accounts.append(account)

    def findAccount(self, accountNumber):
        """This method checks the user's list of accounts to see if the given account number exists, and if so, it returns the account.

        Parameters
        ----------
        accountNumber : int
            Bank account number.

        Returns
        -------
        account
            Returns an account object.
        """
        for account in self.__accounts:
            if account.getAccountNumber() == accountNumber:
                return account
        return None

    def deposit(self, accoutNumber, amount):
        """Deposit an amount into a desired account.

        Parameters
        ----------
        accountNumber : int
            Bank account number.
        amount : float
            Amount to be deposited.
        """

        account = self.findAccount(accoutNumber)
        if account != None:
            if account.deposit(amount):
                print("Transaction completed successfully!")
        else:
            print("No such account exist with Account Number:", accoutNumber)

    def withdraw(self, accoutNumber, amount):
        """Withdraw an amount from a desired account. 

        Parameters
        ----------
        accountNumber : int
            Bank account number.
        amount : float
            Amount to be deposited.
        """
        account = self.findAccount(accoutNumber)
        if account != None:
            if account.withdraw(amount):
                print("Transaction completed successfully!")
        else:
            print("No such account exist with Account Number:", accoutNumber)

    def transfer(self, fromAccountNumber, toAccountNumber, amount):
        """Transfer an amount from one account to another.

        Parameters
        ----------
        fromAccountNumber : int
            Account number from which the amount will be withdrawn.
        toAccountNumber : int
            Account number from which the amount will be received.
        amount : float
            Amount to be deposited.
        """

        fromAccount = self.findAccount(fromAccountNumber)
        toAccount = self.findAccount(toAccountNumber)

        if (fromAccount != None and toAccount != None):
            fromAccount.transfer(toAccount, amount)
            print("Transaction completed successfully!")
        else:
            print("One of the To or From account does not exist")

    def checkBalance(self, accoutNumber):
        """Check the balance of an account. 

        Parameters
        ----------
        accountNumber : int
            Bank account number.
        """
        account = self.findAccount(accoutNumber)
        if account != None:
            print("Balance is: ", account.getBalance())
        else:
            print("No such account exist with Account Number:", accoutNumber)

    @classmethod
    def getNextAccountNumber(cls):
        """Create a new bank account number different from the last account created.

        Returns
        -------
        int
            New bank account number.
        """
        cls.accountNumber += 1
        return cls.accountNumber
