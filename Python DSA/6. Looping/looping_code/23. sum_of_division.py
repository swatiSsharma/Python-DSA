# Sum of division: 
"""
Take two numbers from user
the end range will be n1
check if value is divided by n2 
calculate its total(return)
"""

def sumOfDiv(num1: int, num2: int) -> int:

    i: int = 1
    total: int = 0
    while i <= num1:
        if i % num2 == 0:
            total += i
        i += 1

    return total

n1: int = int(input("Enter the starting range: "))
n2: int = int(input("Enter the ending range: "))

print(sumOfDiv(n1, n2))
print(sumOfDiv(100, 1))
