# Unpacking and Packing 

'''
Unpacking in Python refers to the process of extracting values from iterable objects like tuples, lists, or dictionaries 
and assigning them to individual variables. It is a convenient way to assign multiple values from an iterable to multiple 
variables in a single statement.

Here are examples of unpacking with different types of iterable objects:
'''
## Unpacking a Tuple:
my_tuple = (1, 2, 3)

# Unpacking into individual variables
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

## Unpacking a List:
my_list = [4, 5, 6]

# Unpacking into individual variables
x, y, z = my_list

print(x)  # Output: 4
print(y)  # Output: 5
print(z)  # Output: 6

## Unpacking a String:
my_string = "ABC"

# Unpacking into individual variables
p, q, r = my_string

print(p)  # Output: A
print(q)  # Output: B
print(r)  # Output: C
## Unpacking a Dictionary:
my_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}

# Unpacking keys and values into individual variables
name, age, city = my_dict.values()

print(name)  # Output: Alice
print(age)   # Output: 30
print(city)  # Output: Wonderland
'''
Unpacking can be especially useful when dealing with functions that return multiple values or when working with data 
structures that naturally contain multiple elements. It simplifies the assignment of values to variables in a concise 
and readable manner.
'''

# Packing
'''
Packing in Python refers to the process of combining multiple values into a single variable. This often involves creating 
a tuple or a list to hold the values. It is the opposite operation of unpacking.

Here's an example of packing values into a tuple:
'''
# Packing values into a tuple
my_tuple = 1, 2, 3

# Equivalent to:
# my_tuple = (1, 2, 3)
'''
In this example, the values 1, 2, and 3 are packed into a tuple named my_tuple. The parentheses are optional, and the 
comma is what indicates packing.
'''
'''
Packing is commonly used when you want to group multiple values together. For example, when returning multiple values 
from a function:
'''
def get_coordinates():
    x = 10
    y = 20
    z = 30
    return x, y, z

# Packing the return values into a tuple
coordinates = get_coordinates()

print(coordinates)  # Output: (10, 20, 30)

'''
In this case, the function get_coordinates returns three values, and they are automatically packed into a tuple when 
assigned to the variable coordinates.

Similarly, you can pack values into a list:
'''
# Packing values into a list
my_list = [4, 5, 6]

# Equivalent to:
# my_list = [4, 5, 6]
'''
Packing is a fundamental concept in Python and is used in various situations to group values together for convenient 
storage, passing to functions, or returning from functions.
'''

## The remaining values will be assigned as list for the declared tuple
a, b, *c = (45, 32, 11, 22, 54, 31)

print(a)
print(b)
print(c)

a, *b, c = (45, 32, 11, 22, 54, 31)

print(a)
print(b)
print(c)