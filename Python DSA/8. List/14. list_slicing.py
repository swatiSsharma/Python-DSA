# List slicing
'''
List slicing is a useful feature in Python that allows you to extract a portion of a list. The basic syntax for list slicing is list[start:stop:step], where:

start: The index from which the slicing begins (inclusive).
stop: The index where the slicing ends (exclusive).
step: The step or increment between indices (optional).
Here are some examples:
'''
## Basic Slicing:
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]
print(sliced_list)
# Output: [2, 3, 4]

## Slicing with Step:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = my_list[1:8:2]
print(sliced_list)
# Output: [2, 4, 6, 8]

## Omitting Indices:
'''
If you omit start, it defaults to the beginning; if you omit stop, it defaults to the end.
'''
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[:3]
print(sliced_list)
# Output: [1, 2, 3]

## Negative Indices:
'''
Negative indices count from the end of the list.
'''
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[-3:]
print(sliced_list)
# Output: [3, 4, 5]

'''
'''

## Example usage
my_list = [45, 31, 76, 54, 11, 32, 100]

result = []

for i in range(3,6):
    result.append(my_list[i])

print(result)

# one liner

print(my_list[2: 5])
## Print from specific index to end

print(my_list[2:])
print(my_list[0: 6: 4])

## List slicing creates a shallow copy of the original list, not a deep copy. This means that while the new list created by slicing contains new references to the objects within the original list, it doesn't create new objects for the elements themselves. If the elements of the original list are mutable objects (like other lists), changes to those mutable objects will be reflected in both the original and sliced lists.
'''
Here's an example to illustrate this:
'''
original_list = [1, 2, [3, 4], 5]
sliced_list = original_list[1:3]

# Modify an element within the sliced list
sliced_list[1][0] = 'X'

# Both the original and sliced lists are affected
print(original_list)  # Output: [1, 2, ['X', 4], 5]
print(sliced_list)    # Output: [2, ['X', 4]]
'''
In this example, changing an element within the nested list in sliced_list also affects the corresponding element in original_list. If you need a completely independent copy with no shared references, you would need to use methods like copy.deepcopy() from the copy module.
'''

## If the step is positive the print goes left to right and vice versa in case of negative

print(my_list[0:]) # goes till end from left to right
print(my_list[:])  # same as above
print(my_list[::2]) # even indexes
print(my_list[1::2]) # odd indexes
print(my_list[:5:2])   
print(my_list[::5])
print(my_list[::10])

print(my_list[-4:-1])
print(my_list[-1:-4]) # empty list as Start is large than end
print(my_list[::-1]) # reverse a list

print(my_list[::-2]) # 100, 11, 76, 45

print(my_list[-2:-4:-2]) # 32

print(my_list[-2:-4:2]) # empty list

print(my_list[-5::2]) # 76 11 100

print(my_list[-5::-2])

