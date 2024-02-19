"""
Make 4 functions - add sub, div, mul
ask for input of 
"""

def add():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(f"Addition of two numbers: {num1 + num2}")

def subtract():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(f"Subtract of two numbers: {num1 - num2}")

def multiply():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(f"Multiply of two numbers: {num1 * num2}")

def divide():
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    print(f"Divide of two numbers: {num1 / num2}")


add()
subtract()
multiply()
divide()