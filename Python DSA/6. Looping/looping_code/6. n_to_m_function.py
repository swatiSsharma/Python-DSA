# Write a program to ask m and n from user. Print m to n

def printNumbers(m, n) -> int: 
# do not change the original dataset ie the value of input
    i: int = m
    while i <= n:
        print(i, end = " ")
        i += 1


m: int = int(input("Enter m: "))
n: int = int(input("Enter n: "))
printNumbers(m , n)
