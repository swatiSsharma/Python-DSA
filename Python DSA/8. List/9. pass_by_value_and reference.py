# Pass by Value and reference
'''
In Python, when you pass an argument to a function, the way it behaves can be conceptualized as a 
form of "pass by object reference." However, it's important to understand the distinction between 
mutable and immutable objects to grasp how the argument passing mechanism works.
'''

## Immutable Objects (Pass by Value-Like):
'''
Immutable objects, such as numbers, strings, and tuples, are passed by value-like behavior.
When you pass an immutable object to a function, you are working with a copy of the value, and changes
made inside the function do not affect the original object.
'''
def modify_value(x):
    x += 1
    print("Inside function:", x)

num = 5
modify_value(num)
print("Outside function:", num)


## Mutable Objects (Pass by Reference-Like):  --> sending the memory or id of the list
'''
Mutable objects, such as lists and dictionaries, are passed by reference-like behavior.
When you pass a mutable object to a function, you are working with a reference to the original object,
and changes made inside the function affect the original object.
'''

def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

original_list = [1, 2, 3]
modify_list(original_list)
print("Outside function:", original_list)


'''
In summary:

For immutable objects, changes made inside a function do not affect the original object (pass by 
value-like behavior).
For mutable objects, changes made inside a function affect the original object (pass by reference-
like
 behavior).
It's important to note that the terms "pass by value" and "pass by reference" might not fully capture 
the nuances of Python's argument passing mechanism. Instead, Python's behavior is often described as
 "pass by object reference" or "pass by sharing."
'''
def display(lst: list):
    lst[0] = 100
    print(id(lst))
    print(lst)

my_list = [45, 33, 22, 11, 91]
print(id(my_list))
display(my_list)
print(my_list)