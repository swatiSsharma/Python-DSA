# List Methods

a = [56, 32, 'John', 'Jack', False, 11.11]

# Append -> append(element): Adds an element to the end of the list.
''' Adds element at the end of the list '''

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Extend -> extend(iterable): Appends elements from an iterable (e.g., list, tuple) to the end of the
# list.

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Insert -> insert(index, element): Inserts an element at a specified index.
''' Element is added before the index'''

my_list = [1, 2, 3]
my_list.insert(1, 4)
print(my_list)  # Output: [1, 4, 2, 3]
my_list.insert(-1, 1000)
print(my_list)  # Output: [1, 4, 2, 1000, 3]

# Remove -> remove(element): Removes the first occurrence of a specified element from the list.

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

# Clear -> clear: If you want to remove all elements from a list, you can use the clear() method.

my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # Output: []

# Pop -> pop([index]): Removes and returns the element at the specified index. If no index is 
#                      provided, it removes and returns the last element.

my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2
print(my_list)         # Output: [1, 3]

# Index -> index(element, [start, [end]]): Returns the index of the first occurrence of a specified 
#                                          element in the list.

my_list = [1, 2, 3, 2]
index_of_2 = my_list.index(2)
print(index_of_2)  # Output: 1

# Count -> count(element): Returns the number of occurrences of a specified element in the list.

my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 2

# Sort -> sort(key=None, reverse=False): Sorts the elements of the list in ascending order. You can 
#                                        provide a custom sorting key and set reverse=True for 
#                                        descending order.

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
'''
Timsort is a hybrid sorting algorithm derived from merge sort and insertion sort. It is designed to 
perform well on many kinds of real-world data. The algorithm was implemented by Tim Peters in 2002 
for use in the Python programming language.

Key features of Timsort:

- Adaptive: Timsort is adaptive, meaning it can take advantage of existing order in the input data. 
            If the data is partially ordered, Timsort can benefit from this and perform better.

- Stable: Timsort is a stable sorting algorithm, which means that equal elements maintain their
          relative order in the sorted output.

- Divide and Conquer: Timsort uses a divide-and-conquer strategy, breaking the input into smaller 
                      pieces, sorting them, and then merging the sorted pieces.

- Insertion Sort for Small Arrays: Timsort uses insertion sort for small arrays or subarrays. This is
                                   because insertion sort has lower overhead for small inputs, making
                                   it more efficient in those cases.

- Merge Operation: The merge operation in Timsort is efficient and optimized for merging sorted 
                   sequences. It combines pairs of adjacent sequences, eventually building the
                   fully sorted array.

The most well-known usage of Timsort is in Python's built-in sorted() function and the sort() method for lists. Both of these functions use Timsort to efficiently sort lists of elements.

'''

# Reverse -> reverse(): Reverses the elements of the list in place.

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]

# Copy -> copy(): Returns a shallow copy of the list.

my_list = [1, 2, 3]
copied_list = my_list.copy()
print(copied_list)  # Output: [1, 2, 3]

'''
In Python lists, both del and remove() are used for deleting elements, but they have different 
purposes:
'''
# 1. Using del to Remove by Index: The del statement is used to remove an element from a list based on its index.

my_list = [1, 2, 3, 4, 5]

'''Using del to remove the element at index 2'''
del my_list[2]
print(my_list) # Output: [1, 2, 4, 5]

# 2. Using remove() to Remove by Value: The remove() method is used to remove the first occurrence 
#                                       of a specified value from the list.

my_list = [1, 2, 3, 4, 5]

'''Using remove() to remove the value 3'''
my_list.remove(3)
print(my_list) # Output: [1, 2, 4, 5]

'''
Note that remove() modifies the list in-place and raises a ValueError if the specified value is not 
found.
'''

'''Example Combining del and remove():'''

my_list = [1, 2, 3, 4, 3, 5]

''' Using del to remove the element at index 2'''
del my_list[2]
print(my_list) # Output: [1, 2, 4, 3, 5]

''' Using remove() to remove the value 3 (first occurrence)'''
my_list.remove(3)
print(my_list) # Output: [1, 2, 4, 5]

## Choosing Between del and remove():
'''
- Use del when you know the index of the element you want to delete.
- Use remove() when you know the value of the element you want to delete and want to remove the first 
occurrence.
'''

## Be Careful:
'''
- del modifies the list in-place based on the index.
- remove() modifies the list in-place based on the value.
- Choose the method that fits your specific use case. If you need more control or want to delete
  elements based on a condition, you might consider using list comprehensions or other techniques.

'''