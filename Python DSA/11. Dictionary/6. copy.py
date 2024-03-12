# Copy method in dictionary

# Shallow Copy
'''
In Python, the copy() method for dictionaries creates a shallow copy of the dictionary. This means 
that it creates a new dictionary object containing the same key-value pairs as the original 
dictionary, but the key-value pairs themselves are not copied - they're still references to the same 
objects as in the original dictionary. Here's how you can use the copy() method:
'''
original_dict = {'key1': 'value1', 'key2': 'value2'}
copied_dict = original_dict.copy()
'''
Now, copied_dict contains the same key-value pairs as original_dict, but modifying copied_dict won't 
affect original_dict, and vice versa. However, if the values in the dictionary are mutable objects 
(like lists or other dictionaries), modifying those objects in one dictionary will affect the other 
dictionary, because they are still referencing the same objects.
'''
original_dict = {'key1': [1, 2, 3], 'key2': {'a': 1, 'b': 2}}
copied_dict = original_dict.copy()

##  Modify a value in copied_dict
copied_dict['key1'].append(4)

print(original_dict)  # Output: {'key1': [1, 2, 3, 4], 'key2': {'a': 1, 'b': 2}}

'''
In this example, even though we modified the value of 'key1' in copied_dict, the same list is 
referenced by original_dict['key1'], so the change is reflected in both dictionaries. To avoid such 
scenarios, you may need to perform a deep copy, which creates copies of all nested mutable objects 
as well. This can be achieved using the copy.deepcopy() function from the copy module.
'''

## DeepCopy
'''
The copy module in Python provides the deepcopy() function, which creates a deep copy of an object. 
A deep copy creates a new object with a new memory address for each element in the object being 
, including nested objects. This ensures that changes made to the copied object do not affect the 
original object, even if it contains mutable objects like lists or dictionaries. Here's an example:
'''
import copy

original_list = [1, [2, 3, 4], {'a': 5, 'b': 6}]

# Creating a deep copy of the list
copied_list = copy.deepcopy(original_list)

# Modifying the original list
original_list[1].append(7)
original_list[2]['c'] = 8

# Display the original and copied lists
print("Original List:", original_list)
print("Copied List:", copied_list)

'''
In this example, modifying the original list after creating a deep copy does not affect the copied 
list:
'''

Original List: [1, [2, 3, 4, 7], {'a': 5, 'b': 6, 'c': 8}]
Copied List: [1, [2, 3, 4], {'a': 5, 'b': 6}]

'''
The deepcopy() function recursively creates copies of all nested objects within the original object. 
This is particularly useful when working with complex data structures, ensuring that modifications 
to one instance do not impact another.
'''