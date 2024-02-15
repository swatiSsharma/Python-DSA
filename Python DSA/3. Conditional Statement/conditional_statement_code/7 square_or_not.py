# Take values of length and breadth of a rectangle from user and check if it is square or not

# Ask user for the length and breadth of a rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Check if it is a square or not
if length == breadth:
    print("It is a square.")
else:
    print("It is not a square.")