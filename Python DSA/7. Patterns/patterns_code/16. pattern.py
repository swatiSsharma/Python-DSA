# Pattern 16
'''
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

n: int = int(input("Enter the number: "))

for i in range(n, 0, -1):
    for j in range(i , n+1):
        print(j, end = ' ')
    print()