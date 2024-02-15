# Even or Odd
user_number: float = float(input("Enter a number: "))

# Check if the number is ODD or EVEN
if user_number % 2 == 0:
    print(f"{user_number} is an EVEN number.")
else:
    print(f"{user_number} is an ODD number.")