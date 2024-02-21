# Write a program that takes 2 integers as an arguments (n1,n2), and print all the numbers divisible
# by 3 and 5 between n1 and n2.

n1: int = int(input("Enter the starting range: "))
n2: int = int(input("Enter the ending range: "))

i: int = n1

while  i <= n2:
    if i % 3 == 0 and i % 5 == 0:
        print(i, end = " ")
        i += 1
        
    i += 1
print()


