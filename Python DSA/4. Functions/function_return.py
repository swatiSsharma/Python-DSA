# Return in python function
"""
In Python, the return statement is used to exit a function and return a value to the caller. A 
function can return a single value, multiple values (as a tuple), or no value (in which case None is 
implicitly returned).

Here are examples demonstrating the use of return in Python functions:
"""

# Returning a Single Value:
def add_numbers(x, y):
    result = x + y
    return result

sum_result = add_numbers(3, 5)
print(sum_result)  # Output: 8

# Returning Multiple Values:

def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

numbers = [10, 15, 20, 25]
total_value, average_value = calculate_stats(numbers)
print(f"Total: {total_value}, Average: {average_value}")

# Returning Early in a Function:

def is_positive(number):
    if number > 0:
        return True
    else:
        return False

result = is_positive(7)
print(result)  # Output: True

# Returning None (implicitly):

def print_greeting(name):
    print(f"Hello, {name}!")

result = print_greeting("Alice")
print(result)  # Output: None

"""
In the last example, the function print_greeting does not have a return statement, so it 
implicitly returns None. Functions without an explicit return statement also return None by default.
"""