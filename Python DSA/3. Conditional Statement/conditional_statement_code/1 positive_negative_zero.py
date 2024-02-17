# +ve , -ve or 0

## Variation 1
x = float(input("Enter a number: "))

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")



## Variation 2
x = float(input("Enter a number: "))

if x > 0:
    print("x is positive")
if x < 0:
    print("x is negative")
else:
    print("x is zero")


## Variation 3 (nested if else)
x = float(input("Enter a number: "))

if x >= 0:
    if x == 0:
        print("x is zero")
    else:
        print("x is positive")
else:
    print('x is negative')

## Variation 4 (nested if else)
x = float(input("Enter a number: "))
if x > 0:
    print('x is positive')
else:
    if x == 0:
        print('x is zero')
    else:
        print('x is negative')