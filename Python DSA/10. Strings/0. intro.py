# String
'''
In Python, a string is a sequence of characters enclosed within either single quotes (') or double quotes ("). Strings 
are immutable, meaning once they are created, their contents cannot be changed.

Here are some basics about strings in Python:
'''
# Creating Strings:

# Single quotes
single_quoted_string = 'Hello, World!'

# Double quotes
double_quoted_string = "Hello, World!"

# Triple quotes (used for multi-line strings)
multi_line_string = '''This is a
multi-line
string.'''

# Accessing Characters:
'''
You can access individual characters in a string using indexing:
'''
my_string = "Hello, World!"

print(my_string[0])   # Output: H
print(my_string[7])   # Output: o
print(my_string[-1])  # Output: !
## String Methods:
'''
Strings in Python have numerous built-in methods for various operations like manipulation, searching, formatting, etc. 
Some commonly used methods include:
'''
'''
upper(): Converts the string to uppercase.
lower(): Converts the string to lowercase.
strip(): Removes leading and trailing whitespace.
split(): Splits the string into a list of substrings based on a delimiter.
join(): Joins elements of an iterable (like a list) into a single string.
find(): Returns the lowest index of the substring if found in the string.
replace(): Replaces occurrences of a substring with another substring.
'''

my_string = "   Hello, World!   "

print(my_string.upper())        # Output: "   HELLO, WORLD!   "
print(my_string.strip())        # Output: "Hello, World!"
print(my_string.split(','))     # Output: ['   Hello', ' World!   ']
print('-'.join(['Hello', 'World']))  # Output: "Hello-World"
print(my_string.find('World'))  # Output: 8
print(my_string.replace('World', 'Python'))  # Output: "   Hello, Python!   "

## String Formatting:
'''
Python supports various string formatting methods, including %-formatting, str.format(), and f-strings (introduced in 
Python 3.6).
'''
name = "Alice"
age = 30

# %-formatting
print("Name: %s, Age: %d" % (name, age))

# str.format()
print("Name: {}, Age: {}".format(name, age))

# f-strings
print(f"Name: {name}, Age: {age}")
'''
These are some of the basics of working with strings in Python. Strings are versatile data types and are extensively used 
in various applications, from simple text processing to complex data manipulation.
'''