# Factors count and Prime



def fact(n1: int) -> None:
    i = 1
    count = 0
    while i <= n1:
        if  n1 % i == 0:
            count += 1
        i += 1
    return count

def checkPrime(numberOfFactors: int)  -> bool:
    return fact(numberOfFactors) == 2
     

n1: int = int(input("Enter the num: "))

if checkPrime(n1):
    print(f"{n1} is a prime number")
else:
    print(f"{n1} is not a prime number")
