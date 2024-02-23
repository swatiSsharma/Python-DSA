# Factors of a number

def fact(n1: int) -> None:
    i = 1
    while i <= n1:
        if  n1 % i == 0:
            print(i, end=" ")
        i += 1


n1: int = int(input("Enter the num: "))

fact(n1)
