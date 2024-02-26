# Pattern 5
'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''

n: int = int(input("Enter the number: "))

for i in range(1, n + 1):
    for j in range(n, 0, -1):
        print(j, end=' ')
    print()

# if number are printing differently in output then J will be printed
# if number are printing same in putput the I will be printed