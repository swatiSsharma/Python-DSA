# Control Statement
"""
In Python, break and continue are control flow statements that allow you to alter the flow of a loop,
whether it's a for loop or a while loop.
"""
# break statement:

"""
The break statement is used to exit a loop prematurely. When encountered within the body of a loop, 
it immediately terminates the loop, and the program continues with the next statement after the loop.
"""
for i in range(5):
    if i == 3:
        break
    print(i)

"""
In this example, the loop will print 0, 1, and 2. When i becomes 3, the break statement is executed,
and the loop is terminated.
"""

# continue statement:

"""
The continue statement is used to skip the rest of the code inside a loop for the current iteration 
and proceed to the next iteration.
"""

for i in range(5):
    if i == 2:
        continue
    print(i)

"""
In this example, the loop will print 0, 1, 3, and 4. When i is 2, the continue statement is executed,
skipping the print statement for that iteration and moving on to the next one.
"""
"""
Both break and continue statements provide ways to control the flow of your loops based on certain 
conditions. They are particularly useful for handling specific cases or introducing logic that should 
interrupt the regular iteration process.
"""

"""
Break = get out of the while loop when you want to stop on a specific condition specially useful 
        when you don’t know the input size 
Continue = Skip when you hit that specific condition and then continue executing the rest
"""