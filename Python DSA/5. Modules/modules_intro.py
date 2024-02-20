# Modules
"""
In Python, a module is a file containing Python definitions and statements. The file name is the 
module name with the suffix .py. Modules allow you to organize code into separate files, making it
 more manageable, reusable, and easier to maintain. You can use modules to group related functions, 
 variables, and classes together.

Here's a brief overview of how modules work:
"""
# Creating a Module:
"""
Create a new file with a .py extension.
Define functions, variables, or classes in that file.
"""

# mymodule.py

def greet(name):
    return f"Hello, {name}!"

def add_numbers(x, y):
    return x + y

my_variable = 42

# Using a Module:
"""
Import the module using the import statement.
Access the functions, variables, or classes using the module name.
"""
# main.py

import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
print(mymodule.add_numbers(3, 5))  # Output: 8
print(mymodule.my_variable)  # Output: 42

# Importing Specific Items:
"""
You can import specific functions, variables, or classes from a module.
"""

# main.py

from mymodule import greet, my_variable

print(greet("Bob"))  # Output: Hello, Bob!
print(my_variable)  # Output: 42
# Renaming on Import:
"""
You can use the as keyword to rename modules or items during import.
"""
# main.py

import mymodule as mm

print(mm.greet("Charlie"))  # Output: Hello, Charlie!

"""
Modules are powerful tools for structuring code in larger projects, promoting code reusability, and 
enhancing maintainability. They help in organizing code logically and avoiding naming conflicts 
between different parts of a program.
"""