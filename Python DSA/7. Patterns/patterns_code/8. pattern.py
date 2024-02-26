# Pattern 8
'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''

n: int = int(input("Enter the number: "))

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()