# Ternary operator
'''
In Python, the ternary operator, also known as the conditional expression, provides a concise way to write a simple if-else statement in a single line. The syntax of the ternary operator is:

value_if_true if condition else value_if_false
Here's a simple example:
'''
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
# Output: "Even"

'''
In this example, the value of result is set to "Even" if the condition x % 2 == 0 is True, and "Odd" otherwise.

You can also use the ternary operator for assignments or within expressions. It's a convenient way to write compact and readable code when you need a simple conditional check.

Here's another example with assignment:

'''
is_even = True if x % 2 == 0 else False
print(is_even)
# Output: True
'''
Just keep in mind that while the ternary operator can make code more concise, it's essential to use it judiciously to maintain readability. In more complex scenarios, it might be better to use a regular if-else statement for clarity.
'''

age = 20

print("adult") if age >= 18 else print("child")
## Else part is mandatory
## Is a single line statement
