# Introduction to dictionary

'''
In Python, you can use dictionaries to store key-value pairs. Here's a basic overview of how 
dictionaries work and some common operations you can perform with them:
'''
## Creating a Dictionary:
'''
You can create a dictionary using curly braces {} or the dict() constructor.
'''
### Creating an empty dictionary
my_dict = {}
### or
my_dict = dict()

### Creating a dictionary with initial values
my_dict = {"apple": 2, "banana": 3, "orange": 5}

## Type of dictionary

print(type(my_dict))   ## <class 'dict'>


'''
KEYS SHOULD BE ONLY IMMUTABLE DATA TYPE
'''
## Accessing Values:
'''
You can access the value associated with a key by using square brackets [].
'''
### Accessing value by key
print(my_dict["apple"])  # Output: 2

## Adding or Updating Elements:
'''
You can add new key-value pairs or update existing ones using assignment.
'''
### Adding a new key-value pair
my_dict["grape"] = 4

### Updating an existing value
my_dict["banana"] = 6

## Removing Elements:
'''
You can remove key-value pairs using the del keyword or the pop() method.
'''

### Deleting a key-value pair
del my_dict["orange"]

### Removing and returning the value for a specific key
removed_value = my_dict.pop("banana")

## Iterating Over a Dictionary:
'''
You can iterate over the keys, values, or key-value pairs using various methods such as keys(), 
values(), and items().
'''
### Iterating over keys
for key in my_dict:
    print(key)

### Iterating over values
for value in my_dict.values():
    print(value)

### Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, "->", value)

## Checking for Existence:
'''
You can check if a key exists in a dictionary using the in keyword.
'''
### Checking if a key exists
if "apple" in my_dict:
    print("Yes, 'apple' is in the dictionary.")

## Length of a Dictionary:
'''
You can find the number of key-value pairs in a dictionary using the len() function.
'''
# Finding the length of the dictionary
print(len(my_dict))
'''
These are some of the basic operations you can perform with dictionaries in Python. Dictionaries 
are highly versatile and widely used for various tasks due to their efficiency and flexibility.
'''