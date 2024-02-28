# Update even numbers by 1 and odd numbers by -1

print('Using Index: ')
a = [78, 67, 44, -100, 87, 33, 31]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] += 1
    else:
        a[i] -= 1

print(a)

print('Using Enumerate: ')
a = [78, 67, 44, -100, 87, 33, 31]
for index, value in (enumerate(a)):
    if value % 2 == 0:
        a[index] += 1
    else:
        a[index] -= 1

print(a)