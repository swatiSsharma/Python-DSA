'''
# Statical vs Dynamic typed Language

--> Static Typing:
Variable Types at Compile Time:

In a statically typed language, variable types are determined at compile-time.
The data type of a variable is explicitly declared, and it must be known at the time of compilation.
Compilation checks for type-related errors before the program is run.
Early Error Detection:

Errors related to variable types are caught at compile-time, allowing for early detection and prevention of certain classes of bugs.
It provides better code quality and helps in maintaining code integrity.
Examples:

C, C++, Java, Swift.

--> Dynamic Typing:
Variable Types at Runtime:

In a dynamically typed language, variable types are determined at runtime.
The data type of a variable is not explicitly declared; it is inferred based on the value assigned to the variable.
Late Binding:

The determination of variable types and method calls happens during runtime, allowing for more flexibility in the code.
It provides more dynamic behavior and allows for changes to the type of a variable during execution.
Examples:

Python, JavaScript, Ruby, PHP.
Comparison:
Advantages of Static Typing:

Early error detection.
Better performance as type information is known at compile time.
Improved code readability and maintenance.
Advantages of Dynamic Typing:

Greater flexibility and expressiveness.
Code tends to be shorter and more concise.
Easier to write and understand for some programmers.
Both static and dynamic typing have their advantages and trade-offs. The choice between them often depends on the specific requirements of the project and the preferences of the development team. Some languages also offer a middle ground with optional typing, allowing developers to choose when to use static typing and when to allow dynamic typing.
'''
a = 5
print(a)

a = "Swati"
print(a)

'''
# Annotations: Define what a variable should store

annotations are used to provide additional information about variables, functions, and other objects. Python annotations are not strictly enforced by the interpreter, and they are primarily used for documentation, type hints, and other purposes. There are two main types of annotations in Python:

Variable Annotations:

Variable annotations are used to indicate the expected type of a variable. They are typically used in function signatures, class attributes, or module-level variables.
Example:

age: int = 25
name: str = "John"
In this example, int and str are annotations indicating the expected data types of the variables age and name.
Function Annotations:

Function annotations are used to specify the types of parameters and the return type of a function. They are also used for documentation purposes.
Example:

def add_numbers(a: int, b: int) -> int:
    """
    This function adds two numbers.
    :param a: The first number
    :param b: The second number
    :return: The sum of a and b
    """
    return a + b
In this example, a: int, b: int, and -> int are function annotations indicating the expected types of parameters and the return type.
Annotations in Python are flexible and can be used for various purposes. While they are commonly used for type hints, they can also be used for custom metadata or any information you want to associate with variables and functions. 

'''

a: int = 5
print(a)

a = 4387.980
print(a)

'''
Ek vairable can store among two values 
'''

b: int | float = 55
print(b)

r: int = 10 / 5 # would give error as / will give  result in float not int

#the correct implementation
r: float =  10 / 5