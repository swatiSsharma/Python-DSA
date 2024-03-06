# Single element tuple

'''
In Python, creating a single-element tuple can be a bit tricky because the syntax for creating a tuple involves 
parentheses () and a trailing comma. However, a single-element tuple must have a trailing comma to distinguish it from a 
parenthesized expression.
'''

# Here's how you can create a single-element tuple:
single_element_tuple = (42,)

'''

Note the comma after the element 42. Without the comma, Python will interpret the expression as a simple parenthesized 
expression, not as a tuple.

Here's an example of creating and using a single-element tuple:
'''

single_element_tuple = (42,)

# Accessing the element
print(single_element_tuple[0])  # Output: 42

# Length of the tuple
print(len(single_element_tuple))  # Output: 1

# Iterating through the tuple
for element in single_element_tuple:
    print(element)  # Output: 42

'''
Remember to include the trailing comma when creating a single-element tuple to ensure it is recognized as a tuple by 
Python.
'''
