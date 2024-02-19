# Function

'''
In Python, a function is a block of organized, reusable code that performs a specific task. Functions 
help in modularizing code, making it easier to understand, maintain, and reuse. Here's the basic 
syntax for defining a function in Python:
'''
def function_name(parameters):
    """docstring"""
    # code inside the function
    # optionally, you can use the 'return' statement to return a value

'''
Let's break down the components:

def: keyword used to define a function.
function_name: the name of the function, following the same naming rules as variable names.
parameters: input values that the function accepts (optional).
"""docstring""": a docstring (documentation string) that provides information about the function, its purpose, and usage (optional).
Code block: the actual code that the function executes.
'''

# Function by default always return a value, by default it is None if no explicit return statement is
# provided. In this example, we will create a simple addition function called add_numbers which takes
# two parameters num1 and num2 and returns their sum.

def add_numbers(num1, num2):
    print(num1 + num2)
    return

x = add_numbers(5,6)
print(x)