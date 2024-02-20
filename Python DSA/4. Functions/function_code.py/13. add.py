# Add 3 values using function

# Variation 1
def add( num1: int, num2: int, num3: int):
    a = num1 + num2 + num3
    return a

print("Variation 1")
result = add(56, 78, 46)
print("The sum of the three numbers is : ", result)

# Variation 2

def add( num1: int, num2: int, num3: int):
    a = num1 + num2 + num3
    print(a)
    
print("\nVariation 2")
print("The sum of the three numbers is : ", add(56, 78, 46))
