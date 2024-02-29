# Copy Method -> Shallow and Deep Copy

"""
There are two types of copying: shallow copy and deep copy. Understanding the difference between them 
is important, especially when dealing with nested data structures.
"""

# Shallow Copy: A shallow copy creates a new object, but does not create copies of the nested objects.
#               Instead, it copies references to the nested objects. If the nested objects are mutable
#               (e.g., lists), changes made to the nested objects will be reflected in both the 
#               original and the copied lists.

import copy

original_list = [1, [2, 3], 4]
shallow_copy = copy.copy(original_list)

print("Original List -> ", original_list, 'memory ', id(original_list))
print("Shallow Copy -> ", original_list, 'memory ', id(shallow_copy))

# Modify the nested list in the shallow copy
shallow_copy[1][0] = 'X'

print(original_list)  # Output: [1, ['X', 3], 4]
print(shallow_copy)   # Output: [1, ['X', 3], 4]

# Deep Copy: A deep copy creates a new object and recursively copies all nested objects. Changes made 
#            to the nested objects in the copied list do not affect the original list, and vice versa.

import copy

original_list = [1, [2, 3], 4]
deep_copy = copy.deepcopy(original_list)

print("Original List -> ", original_list, 'memory ', id(original_list))
print("Deep Copy -> ", original_list, 'memory ', id(deep_copy))

# Modify the nested list in the deep copy
deep_copy[1][0] = 'Y'

print(original_list)  # Output: [1, [2, 3], 4]
print(deep_copy)      # Output: [1, ['Y', 3], 4]

"""
In summary:

Shallow copy creates a new object but shares references to nested objects.
Deep copy creates a new object and recursively copies all nested objects, resulting in a completely 
independent copy.
Use shallow copy when you want a new list with references to the same nested objects, and use deep 
copy when you want a new list with copies of all nested objects.
"""

"""
Shallow Copy:
Copies References: A shallow copy creates a new object, but it copies references to the nested objects
rather than creating copies of the nested objects themselves.

Shared References: If the nested objects are mutable (e.g., lists), changes made to the nested objects
will be reflected in both the original and the copied lists, as they share references to the same 
objects.

copy Module: The copy module in Python provides the copy() function for creating shallow copies.

Deep Copy:
Copies Objects: A deep copy creates a new object and recursively copies all nested objects, creating completely independent copies of the original nested objects.

Independent Copies: Changes made to the nested objects in the copied list do not affect the original list, and changes to the original do not affect the copied list. They are entirely independent.

copy Module: The copy module in Python provides the deepcopy() function for creating deep copies.
"""

print("EXAMPLE SITUATION")

import copy
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

b = copy.copy(a)  # Shallow Copy

c = copy.deepcopy(a)  # Deep Copy

print("A ->", a, id(a))
print("B ->", b, id(b))
print("C ->", c, id(c))
b[1] = 1000
b[3][1] = 1000
c[1] = 3000
c[3][1] = 3000
print("A ->", a, id(a))
print("B ->", b, id(b))
print("C ->", c, id(c))