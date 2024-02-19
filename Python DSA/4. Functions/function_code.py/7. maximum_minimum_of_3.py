# Write a Python function to find the Maximum and minimum of three numbers. 
# Use 3 parameters. Make 2 different functions named as maxi and mini

def maxi(num1: float, num2: float, num3: float):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return  num2
    else:
        return num3

def mini(num1: float, num2: float, num3: float):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num3:
        return  num2
    else:
        return num3

# example usgae
num1: float = float(input("Enter first number: "))
num2: float = float(input("Enter second number: "))
num3: float = float(input("Enter third number: "))

max_num = maxi(num1, num2, num3)
min_num = mini(num1, num2, num3)

print(f"The maximum number is {max_num}")
print(f"The minimum number is {min_num}")