# Better solution for count_digits
"""
Time Complexity: O(log10 N), where n is the number of digits

In each iteration of the while loop, the number is divided by 10 (using integer division), effectively
removing the rightmost digit. Since the number of iterations required to reduce the number to 0 is 
proportional to the number of digits in the original integer, and each iteration takes constant time,
the time complexity is logarithmic with respect to the input integer.
This is because the number of iterations required to reduce a number to 0 by dividing it by 10 in 
each step is proportional to the number of digits in the original number, which is approximately 
log10 n. Therefore, the time complexity is O(log 10 n).

Space Complexity: O(1)
"""
import math
def count_digits(number):
    if number == 0:
        return 1  # Special case for zero

    count = 0
    while number != 0:
        count += 1
        number //= 10  # Remove the rightmost digit
    return count

# Test the function
num = 12345
print("Number of digits in", num, ":", count_digits(num))
print(math.log10(500))