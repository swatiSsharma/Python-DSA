

"""
tuple cannot be directly converted to dictionary with 2 values inside it
mandatorily we need to convert it to list to get the dictionary
"""

tup = ('Clara', {'age': 52, 'gender': 'Female'}), ('Eric', {'age': 58, 'gender': 'Male'}), ('John', {'age': 66, 'gender': 'Male'}), ('Swati', {'age': 67, 'gender': 'Female'})

print(dict(tup))

'''
If you have a list of tuples and you want to convert it into a dictionary in Python, you can use the 
dict() constructor or a dictionary comprehension. Here's an example:
'''
# Sample list of tuples
tuple_list = [('Alice', 25), ('Bob', 30), ('Charlie', 22), ('David', 28)]

# Using dict() constructor
dict_from_tuples_1 = dict(tuple_list)

# Using dictionary comprehension
dict_from_tuples_2 = {name: age for name, age in tuple_list}

# Display the resulting dictionaries
print("Dictionary using dict() constructor:", dict_from_tuples_1)
print("Dictionary using dictionary comprehension:", dict_from_tuples_2)
'''
In this example, tuple_list is a list of tuples where each tuple represents a person with their 
name (index 0) and age (index 1).

The dict() constructor can directly convert a list of tuples into a dictionary.

Alternatively, a dictionary comprehension can be used to achieve the same result.

Both methods will produce a dictionary where the names are the keys and the ages are the 
corresponding values. The output of the program will look like:

Dictionary using dict() constructor: {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 28}
Dictionary using dictionary comprehension: {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 

"""
tuple cannot be directly converted to dictionary with 2 values inside it
mandatorily we need to convert it to list to get the dictionary
"""
'''
tup = ('Clara', {'age': 52, 'gender': 'Female'}), ('Eric', {'age': 58, 'gender': 'Male'}), ('John', {'age': 66, 'gender': 'Male'}), ('Swati', {'age': 67, 'gender': 'Female'})

print(dict(tup))

'''
If you have a list of tuples and you want to convert it into a dictionary in Python, you can use the 
dict() constructor or a dictionary comprehension. Here's an example:
'''

# Sample list of tuples
tuple_list = [('Alice', 25), ('Bob', 30), ('Charlie', 22), ('David', 28)]

# Using dict() constructor
dict_from_tuples_1 = dict(tuple_list)

# Using dictionary comprehension
dict_from_tuples_2 = {name: age for name, age in tuple_list}

# Display the resulting dictionaries
print("Dictionary using dict() constructor:", dict_from_tuples_1)
print("Dictionary using dictionary comprehension:", dict_from_tuples_2)

'''
In this example, tuple_list is a list of tuples where each tuple represents a person with their 
name (index 0) and age (index 1).

The dict() constructor can directly convert a list of tuples into a dictionary.

Alternatively, a dictionary comprehension can be used to achieve the same result.

Both methods will produce a dictionary where the names are the keys and the ages are the 
corresponding values. The output of the program will look like:

arduino
Dictionary using dict() constructor: {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 28}
Dictionary using dictionary comprehension: {'Alice': 25, 'Bob': 30, 'Charlie': 22, 'David': 
'''