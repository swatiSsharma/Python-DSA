# The infinite Loop
"""
A loop becomes infinite loop if a condition never becomes FALSE. You must use
caution when using while loops because of the possibility that this condition
never resolves to a FALSE value.
This results in a loop that never ends. Such a loop is called an infinite loop.
"""
# Example 1: Infinite Loop 
x = 1
while x == 1: # This shows an infinite loop
    num = input("Enter a number :")
    print("You entered: ", num)
print("Good Bye!")

# Example 2: Infinite Loop 
num = 10
while num > 1:
    print("Hello")