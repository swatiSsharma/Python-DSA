# Write a Python program to swap the values of two variables without using a temporary variable

num1: int = int(input('Enter the first number: '))
num2: int = int(input('Enter the second number: '))

print("The numbers before swap are {0} and {1}".format( num1, num2))    
num1, num2 = num2, num1

print("The swapped numbers are {0} and {1}".format( num1, num2))