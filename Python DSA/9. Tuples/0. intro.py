# Tuple
'''
A tuple in Python is an immutable, ordered collection of elements. Immutable means that once a tuple is created, its 
elements cannot be changed, added, or removed. Tuples are similar to lists, but they are defined using parentheses () 
instead of square brackets []. Here's an introduction to tuples in Python:
'''

## Creating Tuples
'''
You can create a tuple by enclosing elements within parentheses (). Elements are separated by commas.
'''
# Empty tuple
empty_tuple = ()

# Tuple with elements
my_tuple = (1, 2, 3, 'a', 'b', 'c')

## Accessing Elements
'''
You can access elements of a tuple using indexing or slicing, just like with lists.
'''
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements using indexing
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: a

# Accessing elements using slicing
print(my_tuple[1:4])  # Output: (2, 3, 'a')

## Tuple Packing and Unpacking
'''
Tuple packing is when you create a tuple by assigning values to it. Tuple unpacking is when you assign the values of a 
tuple to multiple variables.
'''

# Tuple packing
my_tuple = 1, 2, 3

# Tuple unpacking
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3

## Immutable Nature
'''
Once a tuple is created, you cannot change its elements.
'''

my_tuple = (1, 2, 3)
my_tuple[0] = 4  # This will raise a TypeError

## Tuple Methods
'''
Tuples have a few methods such as count() and index().
'''
my_tuple = (1, 2, 2, 3, 3, 3)

# Count occurrences of an element
print(my_tuple.count(2))  # Output: 2

# Find index of an element
print(my_tuple.index(3))  # Output: 3

## When to Use Tuples
'''
Use tuples when you want to store a collection of items that should not be changed, such as coordinates or configuration 
settings.
Tuples are also useful for returning multiple values from a function.
'''

# Function returning multiple values
def get_coordinates():
    return 10, 20, 30

x, y, z = get_coordinates()
print(x, y, z)  # Output: 10 20 30

'''
That's a basic introduction to tuples in Python. Tuples are versatile data structures that can be used in various 
situations where immutability is desired.
'''

"""
1. Immutable
2. Everything same as list (index,slicing,iteration)
"""