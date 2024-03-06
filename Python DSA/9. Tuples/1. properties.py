from typing import Tuple

tup: Tuple = (32, 45, -100, 67, 77, 43)

# Access Indexes

print(tup[0])
print(tup[-1])

# update Index/Value
tup[0] = "Hello"
print(tup) # Typeerror: doesnot support item assignment

# Traverse by index or value
for index in range(len(tup)):
    print(tup[index], end = ' ')

for value in tup:
    print(value, end =' ')