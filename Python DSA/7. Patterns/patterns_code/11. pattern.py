# Pattern 11
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''

n: int = int(input("Enter the number: "))

for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(i, end=' ')
    print()