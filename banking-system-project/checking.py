from account import Account


class CheckingAccount(Account):

    def __init__(self, accountNumber):
        # The Python super() method lets you access methods in a parent class and  avoid referring to the base class explicitly.
        super().__init__(accountNumber)
        # Fee that will be applied to each withdrawal and transfer from the current account
        self.__fee = 1.75

    # Overriding the abstract functions of the Account class

    # Deposit
    def deposit(self, amount):
        # Checking if the amount is positive
        if amount > 0:
            self._balance += amount
            return True
        else:
            print("You must deposit a positive amount.")
            return False

    # Withdraw
    def withdraw(self, amount):
        # Checking if the amount is positive
        if amount > 0:
            # Checking if there is enough amount to withdraw
            if (self._balance + self.__fee) >= amount:
                self._balance -= amount
                self._balance -= self.__fee
                #print("Transaction completed successfully!")
                return True
            else:
                print("You do not have a sufficient balance to withdraw $", amount)
        else:
            print("Withdrawal amount must be positive.")
        return False

    # Transfer
    def transfer(self, toAccount, amount):
        # Checking if the amount is positive
        if amount > 0:
            # Checking if there is enough amount to transfer
            if (self._balance + self.__fee) >= amount:
                toAccount.deposit(amount)
                self._balance -= amount
                self._balance -= self.__fee
                return True
            else:
                print("You do not have a sufficient balance to transfer $", amount)
        else:
            print("Transfer amount should be positive.")
        return False
