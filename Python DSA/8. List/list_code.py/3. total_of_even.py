# Total of even number in list

a = [78, 67, 44, -100, 87, 33, 31]
total = 0
for i in a:
    if i % 2 == 0:
        total += i

print(total)