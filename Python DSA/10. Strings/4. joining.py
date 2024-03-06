# Joining in string

'''
In Python, you can join elements of a sequence, like a list, into a single string using the join() method. The join() 
method is a string method that takes an iterable (usually a list of strings) and concatenates its elements into a single 
string, using the calling string as a separator between each element.

Here's the basic syntax:
'''
### separator_string.join(iterable)
'''
separator_string: The string that will be used as a separator between each element in the iterable.
iterable: The sequence of strings you want to join.
Here's an example:
'''
my_list = ["apple", "orange", "banana"]
result_string = ", ".join(my_list)
print(result_string)
# Output: "apple, orange, banana"

'''
In this example, the elements of the my_list are joined into a single string, and the separator , is placed between each 
element.

You can use any string as a separator, and the join() method is not limited to lists; it works with any iterable 
containing strings. Here's another example using a tuple:
'''
my_tuple = ("red", "green", "blue")
result_string = " | ".join(my_tuple)
print(result_string)
# Output: "red | green | blue"
'''
Keep in mind that the join() method is a string method, so it should be called on the separator string and not on the 
iterable.

'''


"""
String -> List
List -> String
"""

my_string = 'python is great'
r = list(my_string)
print(r) ## output -> ['p', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'g', 'r', 'e', 'a', 't']


my_list = [2, 5, 1, 8, 9, 8]
result = str(my_list)
print(type(result), result)  ## output -> <class 'str'> "[2, 5, 1, 8, 9, 8]"
''' Therefore joining the list to string'''


### Whatever needs to be join should be mandatorily be string
result = " ".join(str(i) for i in my_list)
print(result)

my_list = ['a', 'y', 'z', 'q']
result = " ".join(i for i in my_list)
print(result) ## output -> a y z q


my_list = ['a', 'y', 'z', 'q', 1, 2, 3]
result = " ".join(str(i) for i in my_list)
print(result) ## output -> a y z q 1 2 3