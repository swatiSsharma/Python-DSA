# Traverse by Value

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14166.25222]
for i in a:
    print(i)

'''
the loop iterates through each element in the my_list -> a, and the variable value takes on each
element's value during each iteration. You can replace the print(i) line with any operation you want
to perform on each element.
'''

# Traverse by Index

'''
If you want to traverse a list and operate on each element by index, you can use a for loop with 
range() to iterate through the indices of the list. Here's an example:
'''
my_list = [10, 20, 30, 40, 50]

'''Traverse the list and operate on each element by index'''
for index in range(len(my_list)):
    '''Access the element by index and perform some operation'''
    print(f"Index: {index}, Value: {my_list[index]}")
'''
In this example, range(len(my_list)) generates indices from 0 to len(my_list) - 1, and during each 
iteration, the variable index takes on each index value. You can then access the element in the list
using my_list[index] and perform any desired operation.
'''

# Traverse by both index and value
'''
The enumerate() function is a built-in function in Python that allows you to loop over an iterable 
(such as a list) while keeping track of the index and the corresponding value. It returns pairs of 
index and value in each iteration.

Here's how you can use enumerate() to traverse a list by both index and value:
'''
my_list = [10, 20, 30, 40, 50]

# Traverse the list and operate on each element by index and value
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

'''    
In each iteration, index will be the current index, and value will be the corresponding value from 
the list. This is often more concise and readable than using range(len(my_list)) to iterate by 
index.
'''