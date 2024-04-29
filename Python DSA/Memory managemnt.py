a = 10
b = 10
c = 10
d = 10

print(a, b, c, d)
print(id(a), id(b), id(c), id(d))
d = 20

print(a, b, c, d)
print(id(a), id(b), id(c), id(d))


a = [3, 4, 5,6]
b = a

print(a, b)
print(id(a), id(b))

a[0] = 7
print(a, b)
print(id(a), id(b))

b[0] = 8
print(a, b)
print(id(a), id(b))