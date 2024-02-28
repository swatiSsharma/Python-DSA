

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765]
print("Print elements a list: ")
for i in range(0, len(a)):
    print(a[i], end=" ")
print('\n')

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765]
print("Print Alternative elements a list: ")
for i in range(0, len(a), 2):
    print(a[i], end=" ")
print('\n')

# Reverse elements a list 
a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765]
print("Reverse elements a list ")
for i in range(-1, -len(a)-1, -1 ): 
    print(a[i], end=" ")
print('\n')
for i in range(len(a)-1, -1, -1 ): 
    print(a[i], end=" ")
print('\n')