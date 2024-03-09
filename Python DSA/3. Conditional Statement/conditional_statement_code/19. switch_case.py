'''
Programming languages have some conditional / decision-making statements that execute when some specific 
condition is fulfilled.

Switch-case is one of the ways to implement them.

In a menu-driven program, the user is given a set of choices of things to do (the menu) and then is asked 
to select a menu item.

There are 2 choices in the menu:

Choice 1 is to find the area of a circle having radius 'r'.

Choice 2 is to find the area of a rectangle having dimensions 'l' and 'b'.

You are given the choice 'ch' and an array 'a'.

If ‘ch’ is 1, ‘a’ contains a single number ‘r’. If ‘ch’ is 2, ‘a’ contains 2 numbers, ‘l’ and ‘b’.

Consider the choice and print the appropriate area.

Example :
Input: ‘ch’ = 2 and ‘a’ = [3, 2]

Output: area = 6

Explanation: Since the choice ‘ch’ is 2, we have to print the area of the rectangle having ‘l’ = 3 and 
‘b’ = 2, which is 6.
'''
from typing import List
import math

def case_1(a: List[float]) -> float:
    if len(a) == 1:
        area = math.pi * a[0] * a[0]
        return "{:.5f}".format(area)
    else:
        return None  # Handle invalid input for choice 1

def case_2(a: List[float]) -> float:
    if len(a) == 2:
        area = a[0] * a[1]
        return "{:.5f}".format(area)
    else:
        return None  # Handle invalid input for choice 2

def areaSwitchCase(ch: int, a: List[float]) -> float:
    if ch == 1:
        return case_1(a)
    elif ch == 2:
        return case_2(a)
    else:
        return None
    
print(areaSwitchCase(2, [3, 2]))  # Output: 6
print(areaSwitchCase(1, [4]))      # Output: 16.00000