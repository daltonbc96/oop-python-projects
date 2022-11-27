from account import Account


class SavingsAccount(Account):

    def __init__(self, accountNumber):
        super().__init__(accountNumber)
        self.__ir = 0.0375  # 3.75%

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
            if self._balance >= amount:
                self._balance -= amount
               # print("Transaction completed successfully!")
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
            if self._balance >= amount:
                toAccount.deposit(amount)
                self._balance -= amount
                return True
            else:
                print("You do not have a sufficient balance to transfer $", amount)
        else:
            print("Transfer amount should be positive.")
        return True

    # Apply interest rate to account balance
    def applyInterest(self):
        interest = self._balance * self.__ir
        self.deposit(interest)
