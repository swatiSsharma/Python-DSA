'''
Conditional Statement: will give result on condition as boolean

- if: The if statement is used to execute a block of code if a specified condition is true.
- elif(short for "else if"): The if-else statement is used to execute one block of code if the 
  condition is true and another block if the condition is false.
- else: The if-elif-else statement is used when you have multiple conditions to check. It allows you 
  to specify multiple blocks of code to be executed depending on which condition is true.

'''
'''
- Indentation is crucial in Python to define the block of code belonging to the if or else branch.
- elif is short for "else if" and allows you to check additional conditions.
- The else block is optional. If it's not present, the program simply skips to the next code block
  after the if statement.
'''
"""
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false
"""
# Simple if-else statement
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# Nested if-else statement
y = 8

if y > 10:
    print("y is greater than 10")
elif y > 5:
    print("y is greater than 5 but not greater than 10")
else:
    print("y is 5 or less")

# Using if-else in a single line (ternary operator)
result = "even" if x % 2 == 0 else "odd"
print(f"x is {result}")





                              



