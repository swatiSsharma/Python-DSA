# Write a function that prints numbers from 1 to n. The function should take an integer n
# (Print 1 to N). Take N from user


def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i = i + 1
    print()


num: int = int(input("Enter number till where you want to print: "))
printPattern(10)
printPattern(5)
printPattern(47)