# Write a Python program that takes two numbers as input.
# performs the following operations: addition, subtraction, multiplication, division, and modulus.
# Display the results.

num1: int = int(input('Enter the first number: '))
num2: int = int(input('Enter the second number: '))

print("Following are the results:\n ")

print("Addition of {0} and {1}: {2}".format(num1, num2, num1 + num2))
print("Subtraction of {0} and {1}: {2}".format(num1, num2, num1 - num2))
print("Multiplication of {0} and {1}: {2}".format(num1, num2, num1 * num2))
print("Division of {0} and {1}: {2}".format(num1, num2, num1 / num2))
print("Modulus of {0} and {1}: {2}".format(num1, num2, num1 % num2))