# Count the number of factors

def fact(n1: int) -> None:
    i = 1
    count = 0
    while i <= n1:
        if  n1 % i == 0:
            count += 1
        i += 1
    return count

n1: int = int(input("Enter the num: "))

print(fact(n1))
