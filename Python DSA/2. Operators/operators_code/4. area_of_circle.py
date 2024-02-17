# Write a Python program that takes the radius of a circle as input and calculates its area. 
# Use the formula: Area = 3.14 * r ^ 2

radius: float = float(input("Enter the radius of a circle: "))

area = 3.14 * radius ** 2
print('The Area of the circle is {0}'.format(area))