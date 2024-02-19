"""
1. Without Parameters, without Return
2. With Parameters, without Return
3. Without Parameters, with Return
4. With Parameters, with Return
"""

# 1. Without Parameters, without Return
"""
Functions without parameters and without return statements are common when you want to perform a 
specific action or print something without needing any input values or returning a result.
"""
def greet():
    """This function prints a simple greeting."""
    print("Hello, how are you today?")

"""Calling the function"""
greet()

# 2. With Parameters, without Return
"""
Functions with parameters but without return statements are used when you want to perform an action or
provide some output based on the input values but don't need to return a result that will be used 
elsewhere in the code.
"""

def greet_person(name, time_of_day):
    """This function prints a personalized greeting."""
    print(f"Good {time_of_day}, {name}!")

"""Calling the function with arguments"""
greet_person("Alice", "morning")
greet_person("Bob", "afternoon")

# 3. Without Parameters, with Return
"""
Functions without parameters but with return statements are useful when you want to calculate or 
generate a value within the function and provide that result to the part of the code that called the 
function.
"""

def get_random_number():
    """This function returns a random number."""
    import random
    return random.randint(1, 100)

"""Calling the function and storing the result"""
random_number = get_random_number()

"""Printing the result"""
print(f"Random number: {random_number}")

# 4. With Parameters, with Return
"""
Functions with parameters and return statements are commonly used when you want to perform a 
calculation, process input values, and provide a result back to the calling part of the code.
"""

def add_numbers(x: int, y: int):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

"""Calling the function with arguments and storing the result"""
sum_result = add_numbers(5, 7)

"""Printing the result"""
print(f"Sum: {sum_result}")
