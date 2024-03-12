# List in Dictionary

'''
In Python, you can use lists as values in a dictionary. This allows you to associate each key with 
a collection of items. Here's an example:
'''
# Dictionary with lists as values
my_dict = {
    'fruits': ['apple', 'banana', 'orange'],
    'numbers': [1, 2, 3, 4, 5],
    'colors': ['red', 'green', 'blue']
}

# Accessing elements in the dictionary
fruits_list = my_dict['fruits']
numbers_list = my_dict['numbers']

# Modifying the lists
fruits_list.append('grape')
numbers_list.remove(3)

# Displaying the modified dictionary
print("Modified Dictionary:", my_dict)

'''
In this example, my_dict contains three keys ('fruits', 'numbers', and 'colors'), and each key is 
associated with a list as its value. You can access, modify, and perform various operations on these 
lists just like you would with any other list in Python.
'''


'''
Modified Dictionary: {'fruits': ['apple', 'banana', 'orange', 'grape'], 
                     'numbers': [1, 2, 4, 5], 'colors': ['red', 'green', 'blue']}


Keep in mind that the values in a dictionary can be of any data type, including other dictionaries, 
lists, tuples, etc. This flexibility allows you to represent complex data structures using nested 
dictionaries and lists.
'''