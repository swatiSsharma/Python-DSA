# Pass Statement

"""
In Python, the pass statement is a null operation or a no-op. It serves as a placeholder where 
syntactically some code is required, but you don't want to execute any particular instructions. 
It's essentially a way to create a syntactically empty block of code.

Here's an example of how pass might be used:
"""

for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)

"""
In this example, when i is equal to 3, the pass statement is encountered, and it does nothing.
It's often used during development when you're sketching out the structure of your code but haven't 
yet implemented the details. It allows you to have valid syntax without any actual functionality.

"""