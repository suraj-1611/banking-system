import os
from getpass import getpass
from banking import Banking
from config import LOGIN, LOGOUT, DEPOSIT, WITHDRAW, EXIT, CREATE

banking = Banking()

while True:

    print("Welcome to the banking system ...\n")

    if banking.logged_in == False :
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = int (input("Enter your choice: "))

        if choice == LOGIN:
            account_number = input("Enter account number: ")
            password = getpass("Enter password: ")
            if banking.Login(account_number, password):
                print("Login successful and Account Number is ", banking.current_account.account_number)
            else:
                print("Login failed")

        elif choice == CREATE:
            name = input("Enter name: ")
            password = getpass("Enter password: ")
            if banking.CreateAccount(name, password):
                print("Account created successfully and Account Number is ", banking.current_account.account_number)
            else:
                print("Account creation failed")

        elif choice == EXIT:
            break

    else :
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Logout")
    
        choice = int (input("Enter your choice: "))

        if choice == DEPOSIT:
            amount = float(input("Enter amount: "))
            if banking.Deposit(amount):
                print("Deposit successful and Current Balance is ", banking.current_account.balance)
            else:
                print("Deposit failed")
        
        elif choice == WITHDRAW:
            amount = float(input("Enter amount: "))
            if banking.Withdraw(amount):
                print("Withdraw successful and Current Balance is ", banking.current_account.balance)
            else:
                print("Withdraw failed")    

        elif choice == LOGOUT:
            banking.Logout()
            print("Logout successful")