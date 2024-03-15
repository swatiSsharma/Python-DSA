# Map Function
'''
The map() function is used to apply a function to each item in an iterable (such as a list, tuple, or 
set) and return an iterator that yields the results. While map() is commonly used with lists, you can 
also use it with sets.

Here's an example of how you can use the map() function with a set:
'''
# Define a function to square a number
def square(x):
    return x ** 2

# Create a set
my_set = {1, 2, 3, 4, 5}

# Use map() to apply the square function to each element in the set
result = map(square, my_set)

# Convert the result iterator to a set
result_set = set(result)

print(result_set)
# Output: {16, 1, 4, 9, 25}
'''
In this example, the square() function is applied to each element in the set my_set using the map() 
function. The resulting iterator is then converted back to a set using the set() constructor.

While map() can be used with sets, it's important to note that sets are unordered collections, so the 
order of elements in the resulting set may not be the same as the order in the original set.
'''