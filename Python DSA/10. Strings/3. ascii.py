# ASCII in strings

'''
It seems like you might be referring to ASCII strings, which typically means representing text using the ASCII (American 
Standard Code for Information Interchange) character encoding. In ASCII, each character is assigned a unique numerical 
value, ranging from 0 to 127.

Here's a brief explanation:
'''

## ASCII Values:
'''
ASCII assigns a numerical value to each character, including letters, digits, punctuation, and control characters.
For example, the ASCII value for the uppercase letter 'A' is 65, and for the lowercase letter 'a' is 97.
'''

## String to ASCII:
'''
You can obtain the ASCII value of a character in Python using the built-in ord() function.
'''
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of {char} is {ascii_value}")

## ASCII to String:
'''
You can convert an ASCII value to its corresponding character using the built-in chr() function.
'''
ascii_value = 65
char = chr(ascii_value)
print(f"The character with ASCII value {ascii_value} is {char}")

## ASCII String Representation:
'''
In Python, when you work with strings, you're essentially working with a sequence of Unicode characters, which is a more
 extensive character encoding system that includes ASCII.
Python strings can include ASCII characters without any special notation.
'''

my_string = "Hello, ASCII!"
print(my_string)
'''
It's important to note that while ASCII is a subset of Unicode, modern computing often uses Unicode to support a broader 
range of characters from different languages and symbols. The distinction between ASCII and Unicode becomes more apparent
when dealing with characters outside the ASCII range (beyond 0 to 127).
'''