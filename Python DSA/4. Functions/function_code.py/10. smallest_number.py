# Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.

def smallestNumber(num1: float, num2: float, num3: float, num4: float):
    # Determine the smallest number using if-else statements
    if num1 <= num2 and num1 <= num3 and num1 <= num4:
        smallest_number = num1
    elif num2 <= num1 and num2 <= num3 and num2 <= num4:
        smallest_number = num2
    elif num3 <= num1 and num3 <= num2 and num3 <= num4:
        smallest_number = num3
    else:
        smallest_number = num4

    return smallest_number

# Get input from the user for 4 different numbers
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

# Validate that the second number is different from the first
if num2 == num1:
    print("Please enter a different number.")
    num2 = float(input("Enter the second number: "))

num3: float = float(input("Enter the third number: "))

# Validate that the third number is different from the first two
if num3 == num1 or num3 == num2:
    print("Please enter a different number.")
    num3 = float(input("Enter the third number: "))

num4: float = float(input("Enter the fourth number: "))

# Validate that the fourth number is different from the first three
if num4 == num1 or num4 == num2 or num4 == num3:
    print("Please enter a different number.")
    num4 = float(input("Enter the fourth number: "))

result = smallestNumber(num1, num2, num3, num4)
# Print the smallest number
print(f"The smallest number is: {result}")