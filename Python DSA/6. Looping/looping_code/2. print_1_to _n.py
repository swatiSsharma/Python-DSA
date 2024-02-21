# Write a a program prints numbers from 1 to n. The function should take an integer n
# (Print 1 to N). Take N from user

num: int = int(input("Enter number till where you want to print: "))
i: int = 1
while i <= num:
    print(i, end = " ")
    i += 1