# List comprehension
'''
List comprehension is a concise and expressive way to create lists in Python. It provides a more compact syntax for creating lists compared to using traditional loops. The basic structure of a list comprehension is:

new_list = [expression for item in iterable if condition]
expression: The expression to be evaluated and included in the new list.
item: The variable representing each element in the iterable.
iterable: The sequence or iterable you are iterating over.
condition (optional): An optional condition that filters elements based on a specified criteria.
Here are some examples to illustrate list comprehension:
'''

## Basic Example:
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

## List Comprehension with Condition:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Output: [0, 4, 16, 36, 64]

## Nested List Comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Conditional Expression in List Comprehension:
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']
'''
List comprehensions are not only concise but are often considered more readable for simple cases. However, for more complex scenarios or when readability is a concern, using traditional loops may be preferable.
'''

''' It is used to create a list '''
## Optimisation of list for large numbers -- 100000101

my_list = []
my_list = [i for i in range(10)]
print(my_list)

# 1 value numbered list
my_list = []
my_list = [1 for i in range(10)]
print(my_list)

# zero value numbered list
my_list = []
my_list = [0 for i in range(10)]
print(my_list)

my_list = []
my_list = [i+5 for i in range(10)]
print(my_list)

my_list = []
my_list = [i%2 for i in range(1, 11)]
print(my_list)

my_list = []
my_list = [i for i in range(1, 101,5)]
print(my_list)

my_list = []
my_list = [i for i in range(-10, -1, -1)]
print(my_list)


my_list = []
my_list = [i for i in range(10, -1, -1)]
print(my_list)


my_list = []
my_list = [i%2 == 0 for i in range(1,11)]
print(my_list)


my_list = []
my_list = [i for i in range(-10, -1, -1)]
print(my_list)
