"""
Make a function named checkOddEven
Which take 1 integer as an argument

If Integer is Even, then Return True else return False
"""
# brute force solution
def checkOddEven(num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
    
result = checkOddEven(15)
if result == True:
    print("The  number is even")
else:
    print("The number is odd")

# optimal solution 1
def checkOddEven(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False

result = checkOddEven(15)
if result == True:
    print("The  number is even")
else:
    print("The number is odd")

# optimal solution 2
def checkOddEven(num: int) -> bool:
    return num % 2 == 0

result = checkOddEven(15)
if result == True:
    print("The  number is even")
else:
    print("The number is odd")
