# Iterating element in a List

'''
traverse the elements of list
You can iterate through the elements of a list in Python using a for loop or other iterable constructs. Here are a few examples:
'''
## Using a for loop:
my_list = [10, 20, 30, 40, 50]

'''Iterate through elements using a for loop'''
for element in my_list:
    print(element)

## Using range and indexing:

my_list = [10, 20, 30, 40, 50]

'''Iterate through elements using range and indexing'''
for i in range(len(my_list)):
    print(my_list[i])

## Using enumerate to get both index and value:
my_list = [10, 20, 30, 40, 50]

'''Iterate through elements using enumerate'''
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

'''
Choose the method that suits your needs based on whether you need just the values, both the index and
values, or if you have specific requirements for iteration.
'''