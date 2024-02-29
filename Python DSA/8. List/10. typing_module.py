# Typing module
'''
the List type from the typing module in Python. If you're defining a function that takes a list of 
integers as an argument, you can use the List type hint.
'''

from typing import List

def printList(lst: List[int]):
    for index, value in enumerate(lst):
        print(value, index)


# List[int | str]
a: List[int ] = [54, 67, 70, 89]
printList(a)