# Ask 3 numbers from user. Make a function which returns the middle of those 3 numbers. Then make a
# function to check if that middle number is divisible by both 3 and 4. Make 2 functions for 
# reusability.

def middleNumber(num1: int, num2: int, num3: int) -> float:
    return (num1 + num2 + num3)/3

def divisibility(n: float) -> bool:
    return n % 3 == 0 and n % 4 == 0

if __name__ == "__main__":
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    num3: int = int(input("Enter third number: "))

    print(divisibility(middleNumber(num1, num2, num3)))