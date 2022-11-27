from abc import ABC, abstractclassmethod


class Account(ABC):
    """
    This is a class to represent a bank account.

    Methods
    -------
    - deposit: abstract method that will allow making a deposit of an amount in an account.
    - withdraw: abstract method that will allow making a withdrawal from an account.
    - transfer: abstract method to make a transfer from one account to another.
    - getAccountNumber: get function that returns the account number.
    - getBalance: get function that returns the account balance.

    """

    def __init__(self, accountNumber):
        """Initial Constructor.    

        Parameters
        ----------
        accountNumber : int
            Bank account number.
        _balance : float
            Account balance.
        """
        self.__accountNumber = accountNumber  # private variable account number
        self._balance = 0.0  # protected variable balance

    @abstractclassmethod
    def deposit(self, amount):
        """Abstract method that will allow making a deposit of an amount in an account.

        Parameters
        ----------
        amount : float
            Amount to be deposited.
        """
        pass

    @abstractclassmethod
    def withdraw(self, amount):
        """Abstract method that will allow making a withdrawal from an account.

        Parameters
        ----------
        amount : float
            Amount to be withdrawn.
        """
        pass

    @abstractclassmethod
    def transfer(self, toAccount, amount):
        """Abstract method to make a transfer from one account to another.

        Parameters
        ----------
        toAccount : int
            The destination account number of the amount to be transferred.
        amount : float
            Amount to be withdrawn.
        """
        pass

    def getAccountNumber(self):
        """Get function that returns the account number.

        Returns
        -------
        int
            Bank account number.
        """
        return self.__accountNumber

    def getBalance(self):
        """Get function that returns the account balance.

        Returns
        -------
        int
            Account balance.
        """
        return self._balance
