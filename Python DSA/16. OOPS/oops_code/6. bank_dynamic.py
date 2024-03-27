# Bank Dynamic

import random
from typing import List
 
 
class Bank:
    def __init__(self) -> None:
        self.account_number = random.randint(100000, 999999)
        self.holder = input("Enter your name = ").title()
        self.balance = 0.0
        self.account_type = input("Enter account type = ").title()
 
    def display(self):
        print(f"\nAccount number = {self.account_number}")
        print(f"Account holder = {self.holder}")
        print(f"Account balance = {self.balance}")
        print(f"Account Type = {self.account_type}\n")
 
    def withdraw(self):
        amt = float(input("Enter amount to withdraw = "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            print(f"Updated balance = {self.balance}")
        else:
            print("Insuffciient Balance")
 
    def deposit(self):
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt
 
    def getBalance(self):
        print(f"Your balance = {self.balance}")
 
 
accounts: List[Bank] = []
 
 
while True:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit\n")
    choice = int(input("Enter choice = "))
    if choice == 1:
        x = Bank()
        accounts.append(x)
        print(accounts)
    elif choice == 2:
        for obj in accounts:
            obj.display()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")