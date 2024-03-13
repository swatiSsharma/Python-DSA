'''
Write a program to sort the nested list by age
'''

my_list = [["James,76"],["vandana", 23], ["Akul", 67], ["sanjay", 92]]


# based on the element at the first index the list will be sorted
my_list.sort()
print(my_list) # does not return, but changes inside the list


my_list = [["James,76"],["vandana", 23], ["Akul", 67], ["sanjay", 92]]
x = sorted(my_list) # will return a sorted list, can be used with other sequence also
print(x)


## Sort by ascending or descending based on the index  of sub-lists (second elements in each sub-list).
my_list = [["James,76"],["vandana", 23], ["Akul", 67], ["sanjay", 92]]

# Sort
my_list.sort(key=lambda x: x[1]) # sort in ascending
print(my_list)
my_list.sort(key=lambda x: x[1], reverse = True) # sort in descending
print(my_list)

# Sorted
x = sorted(my_list, key=lambda x: x[1])
print(x)