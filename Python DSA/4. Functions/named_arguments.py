# Named Argument

"""
Named arguments make the code more self-explanatory and help avoid mistakes that might occur if the 
order of the arguments is crucial. They are especially useful when working with functions that have a 
large number of parameters or when you want to make your code more readable and maintainable.
"""

def greet_person(name, age, city):
    """This function greets a person with their name, age, and city."""
    print(f"Hello, {name}! You are {age} years old and from {city}.")

# Using named arguments when calling the function
greet_person(name="Alice", age=25, city="Wonderland")
greet_person(city="Cityville", age=30, name="Bob")
