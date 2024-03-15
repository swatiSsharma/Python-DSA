# Methods in Set

'''
Sets in Python have several built-in methods for performing various operations. Here are some common 
methods associated with sets:
'''
## 1. add(): Adds a single element to the set.

my_set = {1, 2, 3}
my_set.add(4)
# Output: {1, 2, 3, 4}

## 2. update(): Adds multiple elements to the set.

my_set.update([4, 5, 6])
# Output: {1, 2, 3, 4, 5, 6}

## 3.remove(): Removes a specified element from the set. Raises a KeyError if the element is not 
#              present.

my_set.remove(3)
# Output: {1, 2, 4, 5, 6}

## 4. discard(): Removes a specified element from the set if it is present. Does not raise an error 
#                 if the element is not present.

my_set.discard(3)
# Output: {1, 2, 4, 5, 6}

## 5. pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is 
#            empty.

popped_element = my_set.pop()
# Output: {2, 4, 5, 6}, popped_element = 1

 ## 6. clear(): Removes all elements from the set.

my_set.clear()
# Output: set()

## 7. copy(): Returns a shallow copy of the set.

new_set = my_set.copy()

'''
These are some of the commonly used methods associated with sets in Python. They provide powerful tools for performing operations on sets efficiently.
'''