# Comments -- ctrl + /

# this is a single line comment. The text between the two slashes will not be executed by python
print("hello World") # this is a print statement


'''Comments are used to provide additional information or 
explanations within the code. Comments are ignored by the 
Python interpreter and are meant for human readers. Here are the main ways to add comments in Python:
'''

# Single-Line Comments: Single-line comments start with the # symbol and continue until the end of the line.

# This is a single-line comment
print("Hello, World!")  # This is an inline comment

# Multi-Line Comments: While Python does not have a specific syntax for multi-line comments, you can use triple-quotes (''' or """) to create a multi-line string, and it is often used as a multi-line comment.

'''
This is a multi-line comment.
It spans multiple lines.
'''
print("Hello, Python!")


"""
Another way to create a multi-line comment.
"""
print("Hello again!")

# Inline Comments: Inline comments are short comments placed at the end of a line of code to provide additional information about that line.

x = 10  # Assigning the value 10 to variable x

# Documentation Strings (Docstrings): Docstrings are used to provide documentation for modules, classes, functions, or methods. They are enclosed in triple-quotes and are accessible using the .__doc__ attribute.

def add_numbers(a, b):
    """
    This function adds two numbers.
    Parameters:
    - a (int): The first number
    - b (int): The second number
    Returns:
    int: The sum of a and b
    """
    return a + b
# Docstrings are commonly used for generating documentation using tools like Sphinx.

 '''-->TODO Comments: Use comments to mark areas in the code that require attention or future work.'''

# TODO: Implement error handling
# This can serve as a reminder for developers working on the codebase.