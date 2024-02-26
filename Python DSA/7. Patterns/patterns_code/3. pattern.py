# pattern 3

'''
*****
*****
*****
*****
*****
'''

n: int = int(input("Enter the number: "))

print("\nVariation 1\n")

for i in range(1, n+1):
    print('* ' * n)

print("\nVariation 2\n")

for i in range(1, n+1):
    for j in range(1, n+1):
        print('*', end=' ')
    print()