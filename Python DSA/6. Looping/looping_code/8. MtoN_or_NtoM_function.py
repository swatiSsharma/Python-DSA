# Take input from user M and N, conditions to print:
"""
If M is less than N, print from M to N
If N is less than M, print from N to M
"""

def printNumbers(num1, num2) -> int: 
# do not change the original dataset ie the value of input
    i: int = num1
    while i <= num2:
        print(i, end = " ")
        i += 1

m: int = int(input("Enter m: "))
n: int = int(input("Enter n: "))

if m <= n:
    printNumbers(m, n)
else:
    printNumbers(n, m)
