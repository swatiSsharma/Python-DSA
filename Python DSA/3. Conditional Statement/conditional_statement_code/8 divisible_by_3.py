# Check if the number entered by User is divisible by 3 or not.

# Ask user for a number
user_number = int(input("Enter a number: "))

# Check if the number is divisible by 3
if user_number % 3 == 0:
    print(f"{user_number} is divisible by 3.")
else:
    print(f"{user_number} is not divisible by 3.")