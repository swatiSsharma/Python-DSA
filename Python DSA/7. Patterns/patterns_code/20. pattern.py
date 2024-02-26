# Pattern 20
'''
1 2 1 2 1
1 2 1 2
1 2 1
1 2
1
'''

n: int = int(input("Enter the number of rows:"))
    
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j%2 == 0:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()