# Inbuilt Function
'''
The min() and max() functions are built-in functions in Python used to find the minimum and maximum values in a sequence, respectively. They can be applied to lists as well. Here are examples:
'''

## Using min() and max() with a list of numbers:

my_list = [10, 20, 30, 40, 50]

'''Find the minimum and maximum values in the list'''
minimum_value = min(my_list)
maximum_value = max(my_list)

print(f"The minimum value in the list is: {minimum_value}")
print(f"The maximum value in the list is: {maximum_value}")

## Using min() and max() with a list of strings:

string_list = ["apple", "banana", "kiwi", "orange", "grape"]

# Find the minimum and maximum values in the list of strings
min_string = min(string_list)
max_string = max(string_list)

print(f"The minimum string in the list is: {min_string}")
print(f"The maximum string in the list is: {max_string}")

'''
These functions are useful for finding extreme values in a list, whether they are numbers or 
strings.

It is only done on homogenoeus or compareable  data types. If you try to use these functions
on lists that contain both numbers and strings, Python would give TypeError.
'''

# Sum
'''
The sum() function is a built-in function in Python that is used to find the sum of all the elements
in an iterable, including lists. Here's an example:
'''

my_list = [10, 20, 30, 40, 50]

# Find the sum of all elements in the list
sum_of_elements = sum(my_list)

print(f"The sum of the elements in the list is: {sum_of_elements}")

'''
The sum() function can be applied to any iterable, such as lists, tuples, and sets. It adds up all the
elements in the iterable and returns the total sum.
'''
# Length in list/ Size of a list

'''
You can determine the length of a list in Python using the len() function. Here's an example:
'''

my_list = [10, 20, 30, 40, 50]

# Get the length of the list
length_of_list = len(my_list)

print(f"The length of the list is: {length_of_list}")

'''
The len() function returns the number of elements in the list, providing a convenient way to obtain 
the size or length of a list.
'''

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14166.25222]
print(f"Length = {len(a)}")
print(f"Maximum = {max(a)}")
print(f"Minimum = {min(a)}")
print(f"Total = {sum(a)}")