# Position odd +1 , even -1

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14166.25222]
for i in range(len(a)):
    if i % 2 == 0:
        a[i] -= 1
    else:
        a[i] += 1
print(a)