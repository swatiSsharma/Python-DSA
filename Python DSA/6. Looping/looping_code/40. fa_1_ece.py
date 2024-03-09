'''
Functions - Take this coding challenge to test your coding skills to

-define a function
-pass arguments by value to a function
-pass arguments by reference to a function

This coding challenge is organized in the following way:

First line of input reads an integer to select the coding challenge:

-Reading value '1' selects the coding-challenge 1 ( tests the ability to define a function and pass arguments 
 by value.)
-Reading value '2' selects the coding challenge 2 (tests the ability to pass arguments by reference to a 
 function)

Coding Challenge -1
Define a function named "Maximum" that accepts two integers (pass by value) as arguments and returns the 
greatest of the two arguments.

Coding Challenge -2
Define a function named "Swap" that accepts two integers (pass by reference) as arguments and swaps their 
value.
'''
import typing as List

def maximum(num1: int, num2: int) ->  int:  # (pass by value)
    if num1 > num2:
        return num1
    else:
        return num2
    
def swapValue(lst: List) -> List:
    num1 = lst[0]
    num2 = lst[1]

    num1, num2 = num2, num1
    return  [num1, num2]

choice: int = int(input("Enter the coding challenge: "))
num1: int = int(input('Enter the first number: '))
num2: int = int(input('Enter the second number: '))

if choice == 1:
    print(maximum(num1, num2))
elif choice == 2:
    print(swapValue([num1, num2]))