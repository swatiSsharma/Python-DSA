# Pattern 7
'''
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''

n: int = int(input("Enter the number: "))

for i in range(n, 0, -1):
    for j in range(1, n+1):
        print(i, end=' ')
    print()