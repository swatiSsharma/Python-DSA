# Escape Sequence ( always comes in "" inside print statment)
# Escape sequences are special sequences of characters used to 
# represent certain invisible or non-printable characters in strings.
# In Python, and many other programming languages, escape sequences 
# begin with a backslash (\). 

'''
\n --> new line ( start or commence with same )
\t --> tab ( four )
\\ --> \
\" --> "
\' --> '
\b --> backspace
\r --> carriage return
'''
print('My name is Ali\nMy age is 18\nMy gender is Male')

# Used for representing a new line.

print("Hello\nWorld")

# Tab (\t): Represents a horizontal tab.

print("First\tSecond\tThird")

# Backslash (\\): Represents a literal backslash.

print("This is a double backslash: \\")

# Single Quote (\') and Double Quote (\"): Used to include single or double quotes within a string.

print('Single quote: \'\nDouble quote: \"')
print('my name is \"Anirudh\"')
print("my name is \"Anirudh\"")
print('M"y n"am"e "i"s "Anirudh"')
print("My ' ' ' ' 'name is 'Anirudh' ")
print("My name is \"Anirudh\" done")
print('My name is \'Anirudh\' done')

# Carriage Return (\r): Represents a carriage return (moves the cursor to the beginning of the line).
""" DocString

A carriage return is an ASCII control character (CR) that typically moves the cursor or printing position to the beginning
of the line. It is represented in Python strings as the escape sequence \r. When encountered in a string, it causes the 
text that follows to overwrite the text that precedes it on the same line.

Here's an example:

print("Hello\rWorld")

Output: Worldlo

In this example, the \r character causes the cursor to return to the beginning of the line after printing "Hello," and then
"World" is printed, overwriting the "Hello" part.
Carriage return is often used in conjunction with line feed (\n) to create a new line. This combination \r\n is a common 
representation of a newline in Windows text files.
It's important to note that the behavior of \r may vary depending on the context in which it is used (e.g., terminal, text
editor, or console). In some environments, it might not produce the expected results, so it's often more common to use \n 
for newline characters.
"""
print("Hello\rWorld")

# Backspace (\b): Represents a backspace.

print("Hello\bWorld")

""" DocString
These escape sequences are useful when you need to include special
characters in strings or control the formatting of output.
"""

# output --> a""\\"xyz'"\
print('a""\\\\"xyz\'"\\')  
print("a\'\\\\\"xyz'\"\\")