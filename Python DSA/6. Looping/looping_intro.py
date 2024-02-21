# Looping
"""
In Python, you can use loops to repeatedly execute a block of code. There are two main types of loops:
- for loops 
- while loops
"""

# for Loop:
"""
The for loop is used when you know in advance how many times you want to execute the code. It iterates
over a sequence (such as a list, tuple, string, or range).
"""

# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Using range to iterate a specific number of times
for i in range(5):
    print(i)

# while Loop:
"""
The while loop is used when you want to repeatedly execute a block of code as long as a certain 
condition is true.
"""

# Example: Printing numbers from 1 to 5 using while loop
count = 1
while count <= 5:
    print(count)
    count += 1

"""
Remember to be cautious with while loops to avoid infinite loops; make sure the condition eventually
becomes false.
"""

# break and continue Statements:
"""
The break statement is used to exit the loop prematurely.

The continue statement is used to skip the rest of the code inside the loop and move to the next 
iteration.
"""

# Example: Using break and continue
for i in range(10):
    if i == 3:
        break  # Exit the loop when i is 3
    if i == 5:
        continue  # Skip the rest of the code and move to the next iteration when i is 5
    print(i)

"""
These examples cover the basics of looping in Python. Depending on your specific needs, you may use 
different types of loops and additional control statements.
"""