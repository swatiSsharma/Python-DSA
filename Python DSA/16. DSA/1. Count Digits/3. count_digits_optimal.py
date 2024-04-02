# Optimal Solution of Count Digits
"""
Time complexity - O(1)
Space complexity - O(1)
"""

import math

def count_digits(number):
    if number == 0:
        return 1  # Special case for zero
    else:
        return int(math.log10(abs(number))) + 1
        # return math.floor((math.log10(abs(number)))) + 1

# Test the function
num = 12345
print("Number of digits in", num, ":", count_digits(num))