# Dictionary methods

'''
Dictionaries in programming languages like Python provide a way to store and organize data using 
key-value pairs. Here are some common methods and operations that can be performed on dictionaries:
'''
## Creating a Dictionary:
my_dict = {'key1': 'value1', 'key2': 'value2'}

## Accessing Values:
value = my_dict['key1']

## Adding or Updating Key-Value Pairs:
my_dict['new_key'] = 'new_value'  # Adding a new key-value pair
my_dict['key1'] = 'updated_value'  # Updating the value of an existing key

## Removing Key-Value Pairs:
del my_dict['key2']  # Deleting a specific key-value pair
my_dict.pop('key1')  # Removing a key-value pair using pop method
my_dict.clear()      # Removing all key-value pairs, making the dictionary empty

## Checking if Key Exists:
if 'key1' in my_dict:
    # Do something

## Getting List of Keys and Values:
keys = my_dict.keys()    # Returns a view of all keys
values = my_dict.values()  # Returns a view of all values

## Getting Items (Key-Value Pairs):
items = my_dict.items()  # Returns a view of all key-value pairs as tuples

## Iterating Through a Dictionary:
for key, value in my_dict.items():
    print(key, value)


## Copying a Dictionary:
new_dict = my_dict.copy()  # Creates a shallow copy of the dictionary

## Merging Dictionaries (Python 3.9 and later):
merged_dict = {**dict1, **dict2}  # Merging two dictionaries

## Dictionary Comprehension:
squared_values = {key: value**2 for key, value in my_dict.items()}
