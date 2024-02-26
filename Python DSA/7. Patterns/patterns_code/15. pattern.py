# Pattern 15
'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''

n: int = int(input("Enter the number: "))
print('\nVariation 1\n')
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        print(j, end=' ')
    print()

print('\nVariation 2\n')

for i in range(n, 0 , -1 ):
    for j in range(n, n - i, -1):
        print(j, end=' ')
    print()