# Chaining in python

my_list = [1, 2, 3, 4, 5]

result = (
    my_list
    .append(6)        # Appends 6 to the list
    .extend([7, 8])   # Extends the list with [7, 8]
    .remove(3)        # Removes the first occurrence of 3
    .sort()           # Sorts the list in ascending order
)

print(my_list)  # Output: [1, 2, 4, 5, 6, 7, 8]
print(result)   # Output: None