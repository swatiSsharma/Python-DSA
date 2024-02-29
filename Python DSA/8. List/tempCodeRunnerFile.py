import copy
a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

b = copy.copy(a)  # Shallow Copy

c = copy.deepcopy(a)  # Deep Copy

print("A ->", a, id(a))
print("B ->", b, id(b))
print("C ->", c, id(c))
b[1] = 1000
b[3][1] = 1000
c[1] = 3000
c[3][1] = 3000
print("A ->", a, id(a))
print("B ->", b, id(b))
print("C ->", c, id(c))