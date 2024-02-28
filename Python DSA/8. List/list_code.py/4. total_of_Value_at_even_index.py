# Total Value at even index

a = [78, 67, 44, -100, 87, 33, 31]
total = 0
for i in range(len(a)):
    if i % 2 == 0:
        total += a[i]

print(total)

a = [78, 67, 44, -100, 87, 33, 31]
total = 0
for i in range(0,len(a),2):
    total += a[i]

print(total)