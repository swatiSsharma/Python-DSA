# Scooping  - visibility
'''
In Python, scoping refers to the rules that determine the visibility and accessibility of variables 
within different parts of your code. Python has two main types of scopes: global scope and local 
scope. 
'''

# Global Scope:

"""
Variables defined outside of any function or class have a global scope.
They can be accessed from any part of the code, including inside functions and classes.
"""
global_variable = 10

def myFunction_global():
    print(global_variable)

myFunction_global()  # Output: 10

# Local Scope:

"""
Variables defined inside a function have a local scope.
They are only accessible within that specific function.
"""

def myFunction_local():
    local_variable = 5
    print(local_variable)

myFunction_local()  # Output: 5

# Trying to access local_variable outside the function would result in an error
# Functions can also access variables from their containing scope (enclosing function or global scope).

def outerFunction():
    outer_variable = 20

    def innerFunction():
        print(outer_variable)

    innerFunction()  # Output: 20

outerFunction()

# Nonlocal Scope:
"""
Variables in an enclosed (non-global) scope can be marked as nonlocal to indicate that they refer to a
variable in the nearest enclosing (non-global) scope.
"""

def outer_function():
    outer_variable = 30

    def inner_function():
        nonlocal outer_variable
        outer_variable += 5
        print(outer_variable)

    inner_function()  # Output: 35

outer_function()

"""
In the example above, nonlocal outer_variable is used to indicate that outer_variable refers to the
variable in the nearest enclosing scope.
Remember that the order of searching for a variable is local scope, then enclosing scopes (if any), 
and finally the global scope. If a variable is not found in any of these scopes, a NameError is 
raised. Understanding scoping is essential for writing clean and maintainable code in Python.
"""

