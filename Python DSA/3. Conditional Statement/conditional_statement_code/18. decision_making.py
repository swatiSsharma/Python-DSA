'''
Programming languages have some conditional / decision-making statements that execute when some specific 
condition is fulfilled.

If-else is one of the ways to implement them.

You are given two numbers 'a' and 'b'.

Compare the numbers and print the relation.

Print “smaller”, “greater” or “equal” when ‘a’ is smaller than ‘b’, greater than ‘b’, or equal to ‘b’ respectively.

Example :
Input: ‘a’ = 5 and ‘b’ = 3

Output: greater

Explanation: Since ‘a’ (= 5) is greater than ‘b’ (= 3), we are printing “greater”.
'''

num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))

if  num1 > num2:
    print("greater")
elif num1 < num2:
    print("smaller")
else:
    print("equal")