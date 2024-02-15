# Type Conversion/ Type Casting
'''
to convert from 1 data type to another
1) String to integer
2)
'''

a = "100"
b = "200"
c = int(a)
d = int(b)

print(a + b)
print(c + d)

a = "100a"
#print(int(a)) # Will give ValueError

a = "100 "
#print(int(a)) # Will get converted


a = "100.9" 
#print(int(a)) # Will give ValueError as it does not know about .


a = int("100")
b = float("200")

print(a, b)

# c = float("200. 500")
# print(c) # ValueError due to space after decimal... if space is at last it would work

d = float("200.500 ")
print(d)


## Float to integer
'''
-  it will always go to lowest integer near to zero, no round off
-  value before decimal will be displayed
'''
a = int(55.56)
print(a) 

print(int(-5.56))

## truthy and falsey value -- BOOL Conversion
#Integer, float and string
print(bool(5))

print(bool(0)) #False

print(bool(1))

print(bool(-555))

print(bool(0.00)) #False

print(bool('')) #False

print(bool(' ')) # true

print(bool('swqd'))

