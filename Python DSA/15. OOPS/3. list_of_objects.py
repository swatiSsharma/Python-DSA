# List of Objects

'''
A list named accounts is created to hold instances of the BankAccount class.
Three BankAccount instances are created and added to the accounts list using the append method.
A loop is used to iterate over the accounts list and display the details of each BankAccount object.
'''

class BankAccount:
    def __init__(self, account_number, account_holder, account_type, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

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
        print(f"Account Type: {self.account_type}")

# Creating a list of BankAccount objects
accounts = []

# Adding BankAccount instances/object to the list
accounts.append(BankAccount("123456789", "Alice", "Saving",balance=1000))
accounts.append(BankAccount("987654321", "Bob", "Current", balance=500))
accounts.append(BankAccount("456789123", "Charlie", "Saving", balance=2000))

# Example usage:
for account in accounts:
    account.display_balance()
    print()