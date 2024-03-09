# ID() function ie Memory Address

'''
The id() function in Python returns the identity (memory address) of an object. It can be
used to check if two variables refer to the same object in memory. Here are various 
scenarios illustrating the use of the id() function:
'''

## How id() Function Work?
'''
the function accepts a single parameter and is used to return the identity of an object. This identity has to 
be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may 
have the same id() value. If we relate this to C, they are the memory address, here in Python it is the unique 
ID. This function is generally used internally in Python. 
'''

  
x = 42
y = x
z = 42
 
print(id(x))  
print(id(y))  # (same as x)
print(id(z))  # (same as x and y)

## Same Object in Memory:

a = [1, 2, 3]
b = a

print(id(a))  # Print the memory address of list a
print(id(b))  # Print the memory address of list b

print(a is b)  # True, because a and b refer to the same object

## Different Objects in Memory:

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # Print the memory address of list a
print(id(b))  # Print the memory address of list b

print(a is b)  # False, because a and b are different objects

## Mutable Objects and Copies:

original_list = [1, 2, 3]
copied_list = original_list.copy()

print(id(original_list))  # Print the memory address of the original list
print(id(copied_list))    # Print the memory address of the copied list

print(original_list is copied_list)  # False, because they are different objects


## Immutable Objects and Reuse of Memory:


x = 42
y = 42

print(id(x))  # Print the memory address of x
print(id(y))  # Print the memory address of y

print(x is y)  # True, because Python may reuse memory for certain integer values

## Function Arguments:


def print_memory_address(obj):
    print(id(obj))

a_list = [1, 2, 3]
print_memory_address(a_list)  # Print the memory address of the list passed as an argument

## Dynamic Object Creation:


def create_and_print_list():
    new_list = [1, 2, 3]
    print(id(new_list))

create_and_print_list()  # Print the memory address of the dynamically created list

'''
The id() function is often used when dealing with mutable objects to confirm whether two 
variables reference the same instance in memory. However, for equality comparisons based 
on values, it's more common to use the equality operators (== and !=).
'''