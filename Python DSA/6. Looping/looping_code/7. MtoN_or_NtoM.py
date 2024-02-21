# Take input from user M and N, conditions to print:
"""
If M is less than N, print from M to N
If N is less than M, print from N to M
"""

m: int = int(input("Enter m: "))
n: int = int(input("Enter n: "))

if m <= n:
    i = m 
    while i <= n:
        print(i, end = " ")
        i += 1 

else:
    i = n
    while i <= m:
        print(i, end = " ")
        i += 1 