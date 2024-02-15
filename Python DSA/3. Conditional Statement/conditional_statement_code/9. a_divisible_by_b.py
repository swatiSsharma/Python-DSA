# Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1: int = int(input("Enter the first number: "))
num2: int = int(input("Enter the second number: "))

if num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")