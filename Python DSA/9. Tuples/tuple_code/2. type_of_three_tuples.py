# Write a program to find the type of three tuples from the inputs given below:
# - "abcdef"
# - 3, 4, 5, 6
# - [11, 12, 13, 14, 15]

tup1 = "abcdef"             #eval(input("Enter the first Tuple: "))
tup2 = 3, 4, 5, 6           #eval(input("Enter the second Tuple: "))
tup3 = [11, 12, 13, 14, 15] #eval(input("Enter the third Tuple: "))

print("First Tuple Data Type is: ",type(tup1))
print("Second Tuple Data Type is: ",type(tup2))
print("Third TupleData Type is: ",type(tup3))


"""
The eval() decides the input type depending upon the given input value, thus, we used tuple() along with 
eval()
"""