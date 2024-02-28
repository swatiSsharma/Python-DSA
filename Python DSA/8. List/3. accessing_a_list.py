# Accessing a list  -- Index

a = [78, 67, 44, -100, 87, 33, 31]

'''
You can access elements in a list using indexing. List indexing starts at 0, so the first element is 
at index 0, the second element at index 1, and so on. Negative indexing is also supported, where -1 
refers to the last element, -2 to the second-to-last element, and so forth.
'''

my_list = [10, 20, 30, 40, 50]

# Accessing elements using positive indexing
first_element = my_list[0]      # 10 (first element)
second_element = my_list[1]     # 20 (second element)
third_element = my_list[2]      # 30 (third element)

# Accessing elements using negative indexing
last_element = my_list[-1]      # 50 (last element)
second_last_element = my_list[-2]  # 40 (second-to-last element)

# Index Error
'''print(my_list[15])'''             # Raises an error because there's no 16th element in the list
''' 
IndexError: list index out of range
An IndexError occurs when you try to access an index in a list that doesn't exist. 
'''

# Slicing to get a subset of elements
subset = my_list[1:4]           # [20, 30, 40] (elements at index 1, 2, 3)
