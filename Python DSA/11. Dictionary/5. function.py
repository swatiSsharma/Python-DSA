# Dictionary Functions

'''
In Python, dictionaries come with built-in methods that allow you to perform various operations on 
dictionaries. Here are some commonly used dictionary methods:
'''
## 1. clear(): Removes all items from the dictionary.
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.clear()

## 2. copy(): Returns a shallow copy of the dictionary.
original_dict = {'key1': 'value1', 'key2': 'value2'}
copied_dict = original_dict.copy()

## 3. get(key, default=None): Returns the value for the specified key. If the key is not found, 
#                             it returns the default value (default is None if not specified).
my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict.get('key1', 'default_value')

## 4. items(): Returns a view of the dictionary's key-value pairs as tuples.
my_dict = {'key1': 'value1', 'key2': 'value2'}
items = my_dict.items()

## 5. keys(): Returns a view of the dictionary's keys.
my_dict = {'key1': 'value1', 'key2': 'value2'}
keys = my_dict.keys()

## 6. values(): Returns a view of the dictionary's values.
my_dict = {'key1': 'value1', 'key2': 'value2'}
values = my_dict.values()

## 7. pop(key, default=None): Removes and returns the value for the specified key. If the key is not 
#                             found, it returns the default value (or raises a KeyError if default is 
#                             not specified).
my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict.pop('key1')


## 8. popitem(): Removes and returns the last key-value pair as a tuple. This is useful when you want 
#                to remove an arbitrary item from the dictionary.
my_dict = {'key1': 'value1', 'key2': 'value2'}
key, value = my_dict.popitem()

## 9. update(iterable): Updates the dictionary with elements from another dictionary or from an 
#                       iterable of key-value pairs.
my_dict = {'key1': 'value1', 'key2': 'value2'}
my_dict.update({'key3': 'value3', 'key4': 'value4'})

## 10. setdefault(key, default=None): Returns the value for the specified key. If the key is not 
#                                     found, inserts the key with a default value (default is None 
#                                     if not specified).
my_dict = {'key1': 'value1', 'key2': 'value2'}
value = my_dict.setdefault('key3', 'default_value')

## 11. fromkeys(iterable, value=None): Creates a new dictionary with keys from the iterable and values
#                                      set to the specified value (default is None if not specified).
keys = ['key1', 'key2', 'key3']
my_dict = dict.fromkeys(keys, 'default_value')

'''
These are just a few of the many methods available for dictionaries in Python. Each method provides 
a way to manipulate or retrieve information from dictionaries, making them powerful and versatile 
data structures.
'''