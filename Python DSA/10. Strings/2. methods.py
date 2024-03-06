# Methods in String
'''
Strings in Python come with a variety of built-in methods that allow you to perform various operations on strings. 
Here are some common string methods:
'''
## capitalize(): Returns a copy of the string with its first character capitalized and the rest lowercased.
my_string = "hello world"
result = my_string.capitalize()
print(result)  # Output: Hello world

## upper(): Returns a copy of the string with all characters in uppercase.
my_string = "hello world"
result = my_string.upper()
print(result)  # Output: HELLO WORLD

## lower(): Returns a copy of the string with all characters in lowercase.
my_string = "Hello World"
result = my_string.lower()
print(result)  # Output: hello world

## title(): Returns a copy of the string with the first character of each word capitalized.
my_string = "hello world"
result = my_string.title()
print(result)  # Output: Hello World

## swapcase(): Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
my_string = "Hello World"
result = my_string.swapcase()
print(result)  # Output: hELLO wORLD

## count(substring): Returns the number of occurrences of a substring in the string.
my_string = "hello world, hello universe"
count = my_string.count("hello")
print(count)  # Output: 2

## find(substring): Returns the lowest index of the first occurrence of a substring in the string. Returns -1 if the 
#                   substring is not found.
my_string = "hello world"
index = my_string.find("world")
print(index)  # Output: 6

## replace(old, new): Returns a copy of the string with all occurrences of the specified substring replaced with another substring.
my_string = "hello world"
result = my_string.replace("world", "universe")
print(result)  # Output: hello universe

## split(separator): Returns a list of substrings obtained by splitting the string at occurrences of the specified separator.
my_string = "apple,orange,banana"
result = my_string.split(",")
print(result)  # Output: ['apple', 'orange', 'banana']

## strip(), lstrip(), rstrip():
'''
strip(): Returns a copy of the string with leading and trailing whitespace removed.
lstrip(): Returns a copy of the string with leading whitespace removed.
rstrip(): Returns a copy of the string with trailing whitespace removed.
'''
my_string = "   hello world   "
result = my_string.strip()
print(result)  # Output: hello world