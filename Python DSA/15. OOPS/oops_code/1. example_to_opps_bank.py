# Bank 
'''
In this example:

The BankAccount class has attributes such as account_number, account_holder, and balance.
The __init__() method is the constructor method, which initializes the object with the provided values.
The deposit() method deposits the specified amount into the account.
The withdraw() method withdraws the specified amount from the account if sufficient balance is available.
The display_balance() method displays the account's details and current balance.
'''
# bank = { 1012349:{'name':'xyz',
#                   'age':18,
#                   'branch':'abc',
#                   'balance': 0
#                   }
#         }

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} successfully processed.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully processed.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

# Example usage:
account1 = BankAccount("123456789", "Alice")
account1.display_balance()  # Output: Account Number: 123456789, Account Holder: Alice, Current Balance: 0

account1.deposit(1000)  # Output: Deposit of 1000 successfully processed.
account1.display_balance()  # Output: Account Number: 123456789, Account Holder: Alice, Current Balance: 1000

account1.withdraw(500)  # Output: Withdrawal of 500 successfully processed.
account1.display_balance()  # Output: Account Number: 123456789, Account Holder: Alice, Current Balance: 500
