
# --------------------------------------------------------
# DBC Bank system
# Written by Dalton Costa
# November, 2022

#This is a Python project for practicing object-oriented programming concepts. 
#With this project it is possible for the user to create a checking or savings account and perform financial transactions between accounts.
#This project includes classes and methods for creating accounts and performing financial transactions.
# --------------------------------------------------------

from account import Account
from checking import CheckingAccount
from savings import SavingsAccount
from client import Client

""" 
This file contains the user interaction routines, and it is dependent on the methods created in the other files of this project. 
When you execute this file, the terminal will provide you with many choices for interacting with the system.

Methods
-------
    - menu: creates the main menu that shows the user all action options.
    - createAccount: creates a menu with the different types of accounts that the user can create.
    - checkBalance: allows the user to check the balance of the account provided.
    - doDeposit: allows the amount to be deposited into the specified account.
    - doWithdraw: allows the amount to be withdrawn from the provided account.
    - doTransfer: allows the transfer of the amount from one account to another. 
"""
# Main Menu


def menu():
    """Creates the main menu that shows the user all action options.

    This function displays the user's Main Menu options view, 
    collects, and returns the option selected by the user.

    Returns
    -------
    int
        Returns the value that represents the user's selected option.

    """

    choice = -1

    while choice < 0 or choice > 5:
        print()
        print("  ┌────────────────┐  ╭───────────────────────╮           ")
        print("  │  ╭┼┼╮          │  │ ▶︎ 1 • Create Account  │          ")
        print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
        print("  │  ╰┼┼╯          │  │ ▶︎ 2 • Check Account Balance │    ")
        print("  │                │  ├────────────────────────────┬╯     ")
        print("  │  DBC           │  │ ▶︎ 3 • Deposit an Amount    │     ")
        print("  │  B A N K       │  ├───────────────────────────┬╯      ")
        print("  │                │  │ ▶︎ 4 • Withdraw an Amount  │      ")
        print("  │                │  ├───────────────────────────┴╮      ")
        print("  │ ║│┃┃║║│┃║│║┃│  │  │ ▶︎ 5 • Transfer an Amount   │     ")
        print("  │ ║│┃┃║║│┃║│║┃│  │  ├────────────────────┬───────╯      ")
        print("  │                │  │ ▶︎ 0 • Exit System  │             ")
        print("  └────────────────┘  ╰────────────────────╯              ")
        print()
        choice = int(input("\n  ☞ Enter your command: "))

    return choice


# Create an account
def createAccount(client):
    """Creates a menu with the different types of accounts that the user can create.

    This function displays the account types that the user may create. The user can create as many accounts as they want depending on the account type, 
    with the number being one digit different from the last account created.
    Furthermore, it saves and returns the user's selection.

    Parameters
    ----------
    client : client
        This function expects to receive objects of type client that contain all the user's account information.

    Returns
    -------
    int
        Returns the value that represents the user's selected option.

    """

    # Menu to user to select account type
    choice = -1

    while choice < 0 or choice > 2:

        print()
        print("  ┌────────────────┐  ╭───────────────────────╮           ")
        print("  │  ╭┼┼╮          │  │ Select Account Type   │          ")
        print("  │  ╰┼┼╮          │  ├───────────────────────┴─────╮     ")
        print("  │  ╰┼┼╯          │  │ ▶︎ 1 • Checking Account      │     ")
        print("  │                │  ├────────────────────────────┬╯     ")
        print("  │  DBC           │  │ ▶︎ 2 • Savings Account      │      ")
        print("  │  B A N K       │  ├───────────────────────────┬╯      ")
        print("  │                │  │ ▶︎ 0 • Back to main        │       ")
        print("  │                │  ╰───────────────────────────╯       ")
        print("  │ ║│┃┃║║│┃║│║┃│  │                                      ")
        print("  │ ║│┃┃║║│┃║│║┃│  │                                      ")
        print("  │                │                                      ")
        print("  └────────────────┘                                      ")
        print()
        choice = int(input("\n  ☞ Enter your command: "))

    print()

    if choice == 1:
        checking = CheckingAccount(client.getNextAccountNumber())
        client.addAccount(checking)
        print("Successfully created a Checking account - Account Number: ",
              checking.getAccountNumber())
    elif choice == 2:
        savings = SavingsAccount(client.getNextAccountNumber())
        client.addAccount(savings)
        print("Successfully created a Savings account - Account Number: ",
              savings.getAccountNumber())


# check balance
def checkBalance(client):
    """Allows the user to check the balance of the account provided.    

    Parameters
    ----------
    client : client
        This function expects to receive objects of type client that contain all the user's account information.

    """
    accountNumber = int(input("Enter Account Number: "))
    client.checkBalance(accountNumber)

# Deposit function


def doDeposit(client):
    """Allows the amount to be deposited into the specified account.    

    Parameters
    ----------
    client : client
        This function expects to receive objects of type client that contain all the user's account information.

    """
    accountNumber = int(input("Enter Account Number: "))
    amount = float(input("Enter an Amount to deposit: "))
    client.deposit(accountNumber, amount)

# Withdraw function


def doWithdraw(client):
    """Allows the amount to be withdrawn from the provided account.    

    Parameters
    ----------
    client : client
        This function expects to receive objects of type client that contain all the user's account information.

    """
    accountNumber = int(input("Enter Account Number: "))
    amount = float(input("Enter an Amount to Withdraw: "))
    client.withdraw(accountNumber, amount)

# Transfer function


def doTransfer(client):
    """Allows the transfer of the amount from one account to another.    

    Parameters
    ----------
    client : client
        This function expects to receive objects of type client that contain all the user's account information.

    """
    fromAccountNumber = int(input("Enter From Account Number: "))
    toAccountNumber = int(input("Enter To Account Number: "))
    amount = float(input("Enter an Amount to Transfer: "))
    client.transfer(fromAccountNumber, toAccountNumber, amount)


if __name__ == '__main__':

    client = Client()

    choice = -1

    while choice != 0:
        choice = menu()
        print()

        if choice == 1:  # Create account
            createAccount(client)
        elif choice == 2:  # check balance
            checkBalance(client)
        elif choice == 3:  # deposit
            doDeposit(client)
        elif choice == 4:  # withdrawal
            doWithdraw(client)
        elif choice == 5:  # transfer
            doTransfer(client)
        else:
            print("GoodBye!...")
