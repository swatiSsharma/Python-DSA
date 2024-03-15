# Type Conversion in Set

'''
In Python, you can perform type conversions involving sets. Here are some common type conversions:
'''
## Converting List to Set:
'''
You can convert a list to a set using the set() constructor. This removes any duplicate elements from 
the list and creates a set containing unique elements.
'''
my_list = [1, 2, 3, 3, 4, 5]
my_set = set(my_list)
# Output: {1, 2, 3, 4, 5}

## Converting String to Set:
'''
You can convert a string to a set to get a set of its characters.
'''
my_string = "hello"
my_set = set(my_string)
# Output: {'h', 'e', 'l', 'o'}

## Converting Set to List:
'''
You can convert a set to a list using the list() constructor.
'''
my_set = {1, 2, 3}
my_list = list(my_set)
# Output: [1, 2, 3]

## Converting Set to Tuple:
'''
You can convert a set to a tuple using the tuple() constructor.
'''
my_set = {1, 2, 3}
my_tuple = tuple(my_set)
# Output: (1, 2, 3)

## Converting Set to String:
'''
You can convert a set to a string, but since sets are unordered collections, the order of elements in 
the resulting string may vary.
'''
my_set = {'a', 'b', 'c'}
my_string = str(my_set)
# Output: "{'a', 'b', 'c'}"
'''
These are some common type conversions involving sets in Python. They allow you to manipulate data 
between different data types effectively.
'''