# Lambda functions
'''Anonymous functions'''

'''
Lambda functions in Python are anonymous, one-liner functions defined using the lambda keyword. Unlike 
regular functions defined with the def keyword, lambda functions are typically used for short-term and 
specific purposes. Here are some key points about lambda functions:
'''
# Syntax: The basic syntax of a lambda function is:

## ->  lambda arguments: expression


add = lambda x, y: x + y

'''Here, x and y are the parameters, and x + y is the expression.'''

## Anonymous Functions:
'''
Lambda functions are often referred to as anonymous functions because they don't have a name like 
regular functions. They are usually used where a small, unnamed function is required for a short 
duration.
'''

## Single Expression:
'''
Lambda functions can only contain a single expression. The result of this expression is implicitly 
returned.

Use Cases:
Lambda functions are commonly used in situations where a small function is needed temporarily, such 
as for filtering, mapping, or sorting data. They are frequently employed with functions like map(), 
filter(), and sorted().
'''

# Example using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

## Functional Programming:
'''
Lambda functions align well with the principles of functional programming. They can be passed as 
arguments to higher-order functions and used in functional constructs.
'''
# Example using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

## Limitations:
'''
While lambda functions are convenient for simple tasks, they are limited compared to regular 
functions. They lack features like docstrings and multiple expressions.
'''

## Readability:
'''
While lambda functions can be concise, they should be used judiciously to maintain code readability. 
For complex logic, it's often better to use a regular named function.
'''
# Example using a regular function
def add_function(x, y):
    return x + y

'''
In summary, lambda functions in Python are a concise way to define small, temporary functions. They 
are particularly useful in functional programming constructs and when brevity is essential. However, 
for more complex or frequently used functions, regular named functions are generally preferred for 
better code organization and readability.
'''


'''
In Python, you can use lambda functions within dictionaries to define functions on the fly, especially 
when you need to create concise and short-lived functions. Here's an example of how you can use lambda
functions in a dictionary:
'''
# Define a dictionary with lambda functions
operation_dict = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Cannot divide by zero'
}

# Example usage
result_add = operation_dict['add'](5, 3)
result_subtract = operation_dict['subtract'](8, 2)
result_multiply = operation_dict['multiply'](4, 6)
result_divide = operation_dict['divide'](10, 2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)

'''
In this example, the dictionary operation_dict contains keys ('add', 'subtract', 'multiply', 'divide')
associated with lambda functions that perform the corresponding mathematical operations. The lambda 
functions take two arguments (x and y) and return the result of the operation.
'''