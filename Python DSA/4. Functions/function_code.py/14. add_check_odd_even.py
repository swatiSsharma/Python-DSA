# Create two function and check odd and even
"""
- Make 2 function add and checkOddEven
- the output of add will be the input for checkOddEven function
"""

def add( num1: int, num2: int, num3: int) -> int:
    a = num1 + num2 + num3
    return a

def checkOddEven(num: int) -> None:
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

result = add(45,67,89)
checkOddEven(result)

# Print vs Return
'''
The print and return statements serve different purposes in functions.

1) print Statement:

- The print statement is used to display information on the console.
- It is primarily for debugging purposes or providing output to the user.
- It does not affect the flow of the program, and the printed values are shown on the console.

2) return Statement:

- The return statement is used to exit a function and send a value (or values) back to the caller.
- It is used to produce a result or output that can be further used in the program.
- When a function encounters a return statement, it immediately exits, and the value after return is
  sent back to the caller.

In summary, print is used for displaying information, whereas return is used for producing a result 
or value that can be used in the rest of the program. Functions can have both print and return 
statements, but their purposes are distinct.
'''
