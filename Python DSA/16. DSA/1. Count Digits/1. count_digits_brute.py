# Brute Force for count_digits
""" 
Time Complexity - O(N) ie conversion of int to str
Space Complexity - O(1)
"""

def count_digits(number):
    # Convert the number to a string
    number_str = str(number)
    # Return the length of the string, which represents the number of digits
    return len(number_str)

# Test the function
num = 12345
print("Number of digits in", num, ":", count_digits(num))