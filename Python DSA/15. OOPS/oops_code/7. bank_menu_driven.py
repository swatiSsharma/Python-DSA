# Bank Menu Driven

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
            print(f"Withdrawal of {amt} successful")
            print(f"Updated balance = {self.balance}")
        else:
            print("Insufficient Balance")

    def deposit(self):
        amt = float(input("Enter amount to deposit = "))
        if amt < 0:
            print("Invalid amount")
            return
        self.balance += amt
        print(f"Deposit of {amt} successful")
        print(f"Updated balance = {self.balance}")

    def getBalance(self):
        print(f"Your balance = {self.balance}")

    def transfer(self, recipient_account):
        amt = float(input("Enter amount to transfer = "))
        if amt < 0:
            print("Invalid amount")
            return
        if self.balance >= amt:
            self.balance -= amt
            recipient_account.balance += amt
            print(f"Transfer of {amt} successful")
            print(f"Your updated balance = {self.balance}")
        else:
            print("Insufficient Balance")

accounts: List[Bank] = []

while True:
    print("\n1. Add account")
    print("2. Display all accounts")
    print("3. Search account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Get balance")
    print("7. Transfer")
    print("8. Exit\n")

    choice = input("Enter your choice = ")

    # Validate the input
    try:
        choice = int(choice)  # Convert the input to an integer
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        x = Bank()
        accounts.append(x)
        print(accounts)

    elif choice == 2:
        for obj in accounts:
            obj.display()

    elif choice == 3:
        search_acc = int(input("Enter Account number to search = "))
        found = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.display()
                found = True
                break
        if not found:
            print("Account not found!")

    elif choice == 4:
        search_acc = int(input("Enter Account number to deposit = "))
        found = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.deposit()
                found = True
                break
        if not found:
            print("Account not found!")

    elif choice == 5:
        search_acc = int(input("Enter Account number to withdraw = "))
        found = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.withdraw()
                found = True
                break
        if not found:
            print("Account not found!")

    elif choice == 6:
        search_acc = int(input("Enter Account number to check balance = "))
        found = False
        for obj in accounts:
            if obj.account_number == search_acc:
                obj.getBalance()
                found = True
                break
        if not found:
            print("Account not found!")

    elif choice == 7:
        search_sender = int(input("Enter sender Account number = "))
        search_recipient = int(input("Enter recipient Account number = "))
        found_sender = False
        found_recipient = False
        sender_account = None
        recipient_account = None

        for obj in accounts:
            if obj.account_number == search_sender:
                sender_account = obj
                found_sender = True
            elif obj.account_number == search_recipient:
                recipient_account = obj
                found_recipient = True

            if found_sender and found_recipient:
                break

        if not found_sender or not found_recipient:
            print("Sender or recipient account not found!")
        else:
            sender_account.transfer(recipient_account)

    elif choice == 8:
        break
    else:
        print("Invalid Choice")
