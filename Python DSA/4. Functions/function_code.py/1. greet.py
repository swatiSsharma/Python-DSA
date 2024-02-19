# Greet function

def greet():
    print("Hello, welcome to the program!")

def greet_person(name):
    """This function greets a person."""
    print(f"Hello, {name}!")

def greet_optimal(name="Guest"):
    """This function greets a person."""
    print(f"Hello, {name}!")

greet()          # Output: Hello, welcome to the program!
greet_person("Alice")   # Output: Hello, Alice!
greet_optimal("hello") # Output: Hello, hello!
greet_optimal()   # Output: Hello, Guest!