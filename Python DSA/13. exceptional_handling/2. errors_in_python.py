# Errors in Python

'''
Python errors can vary widely depending on the nature of the code and the circumstances under which 
it's executed. Here are a few common errors you might encounter in Python:
'''
# 1) SyntaxError: This error occurs when the Python parser encounters invalid syntax in your code. It 
#              typically indicates a mistake in your code that prevents it from being parsed correctly.

if x = 5:  # SyntaxError: invalid syntax (should be 'if x == 5:')
    print("x is 5")

# 2) IndentationError: Python uses indentation to define block structures such as loops and conditional
#                      statements. An IndentationError occurs when there's a problem with the 
#                      indentation of your code.

for i in range(5):
print(i)  # IndentationError: expected an indented block


# 3) NameError: This error occurs when you try to access a variable or function name that hasn't been 
#             defined yet. A NameError will also occur if you attempt to call a method on an object  
#             without first defining the object itself.

print(x)  # NameError: name 'x' is not defined

# 4) TypeError: This error occurs when an operation is performed on an object of inappropriate type.

print(5 + "hello")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 5) ValueError: This error occurs when a function receives an argument of the correct type but with 
#                an inappropriate value.

int("hello")  # ValueError: invalid literal for int() with base 10: 'hello'

# 6) IndexError: This error occurs when you try to access an index that doesn't exist in a sequence 
#                (such as a list or a string).
my_list = [1, 2, 3]
print(my_list[3])  # IndexError: list index out of range

# 7) KeyError: This error occurs when you try to access a dictionary key that doesn't exist.
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # KeyError: 'c'

# 8) AttributeError: This error occurs when you try to access or use an attribute or method that does 
#                    not exist for a given object.

my_list = [1, 2, 3]
my_list.foo()  # AttributeError: 'list' object has no attribute 'foo'

# 9) FileNotFoundError: This error occurs when you try to open or access a file that does not exist.

with open('nonexistent_file.txt', 'r') as file:
    content = file.read()  
    # FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

# 10) ImportError: This error occurs when Python cannot find the module or package you're trying to 
#                  import.

import non_existent_module  # ImportError: No module named 'non_existent_module'

# 11) ZeroDivisionError: This error occurs when you try to divide a number by zero.
result = 10 / 0  # ZeroDivisionError: division by zero

# 12) AssertionError: This error occurs when an assert statement fails.
x = 10
assert x == 5  # AssertionError

# 13) TypeError (unsupported operand type(s)): This error occurs when an operation is performed on 
#                                              objects of incompatible types.

'hello' + [1, 2, 3]  # TypeError: can only concatenate str (not "list") to str

# 14) RecursionError: This error occurs when the maximum recursion depth is exceeded. It typically 
#                     happens in recursive functions that don't have a proper termination condition.

def countdown(n):
    print(n)
    countdown(n-1)

countdown(10**6)  # RecursionError: maximum recursion depth exceeded in comparison

# 15) KeyboardInterrupt: This error occurs when the user interrupts the execution of a Python program 
#                        using a keyboard interrupt signal (e.g., pressing Ctrl+C).

while True:
    pass  # Press Ctrl+C to generate KeyboardInterrupt