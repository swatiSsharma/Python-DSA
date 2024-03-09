'''
Data type refers to the type of value a variable has and the way the computer interprets it.

Each data type has a different size. You’ve studied 5 different data types and the sizes of the data 
types:

Integer: 4 bytes
Long: 8 bytes
Float: 4 bytes
Double: 8 bytes
Character: 1 byte

You’re given a data type. Print its size in bytes.

Example :
Input: Long

Output: 8

Explanation: The size of a Long variable is given as 8 bytes.
'''

def dataType(str1: str) -> int:
    if str1.lower() == "integer":
        return 4
    elif str1.lower() == "long":
        return 8
    elif str1.lower() == "float":       
        return 4
    elif str1.lower() == "double":      
        return 8
    elif str1.lower() == "character":
        return 1
    else:
        return -1
    
print(dataType("Long"))
print(dataType("Decimal"))
print(dataType('Float'))