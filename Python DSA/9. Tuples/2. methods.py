# Methods in Tuples

'''
Tuples in Python are immutable, which means once they are created, their elements cannot be modified. Therefore, tuple 
objects have a limited set of methods compared to mutable data structures like lists. Here are the primary methods 
available for tuples:
'''
## count(value): Returns the number of occurrences of a specified value in the tuple.
my_tuple = (1, 2, 2, 3, 3, 3)
print(my_tuple.count(2))  # Output: 2

## index(value, start, end): Returns the index of the first occurrence of the specified value within the given range 
#  (start and end).

my_tuple = (1, 2, 2, 3, 3, 3)
print(my_tuple.index(3))  # Output: 3

## membership operator

my_tuple = (1, 2, 2, 3, 3, 3)
print(3 in my_tuple) # Output: True
print(4 in my_tuple) # Output: False

## Slicing
my_tuple = (1, 2, 2, 3, 3, 3)
print(my_tuple[1:4])
print(my_tuple[::-1]) #reversed tuple

## Combining tuples
a = (1, 2, 3)  
b = ('A', 'B')
c = a + b       #Output: (1, 2, 3, 'A', 'B')
d = a * 3      #Output      : (1, 2, 3, 1, 2, 3)
e = b + ("C", )#Output      : ('A', 'B', 'C')
f = c * 0     #Output         : ()
g = "".join(e) #Output        : ABCC4   
h = "%s-%s" % (e[0], e[1]) #Output: A-B
               #Note    that it joins elements with nothing between them.

print(a,b,c,d,e,f,g,h, end ='\n')

'''
It's important to note that tuples do not have methods for adding or removing elements because of their immutable nature. 
If you need to perform such operations, you may want to use a list instead.

Here's a summary of the available tuple methods:

count(value): Returns the number of occurrences of a specified value.
index(value, start, end): Returns the index of the first occurrence of a specified value within the given range.
These methods provide useful functionality for working with tuples, allowing you to query their contents without modifying
them.
'''