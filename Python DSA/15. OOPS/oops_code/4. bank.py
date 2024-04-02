# Bank Class

import random

class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name: ")
        self.balance = 0
        self.account_type = input("Enter account type: ")
    
    def display_account_info(self):
        print(f"\nAccount Holder: {self.holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}\n")

    def deposit(self):
        amount = float(input("Enter amount to  deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successfully processed.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("Enter amount to  withdraw: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully processed.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def getBalance(self):
        print(f"Your Balance is:  ${self.balance:.2f}")


b1 = Bank()
b1.display_account_info()
b1.deposit()
b1.withdraw()
b1.getBalance()