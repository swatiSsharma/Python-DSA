# Optimal Solution for Reverse a number

'''
An optimal solution to reverse a number without converting it to a string can be achieved using 
arithmetic operations, similar to the previous approach. However, we can make a slight improvement 
by avoiding unnecessary integer division and modulo operations.
'''
"""
Time Complexity: O(log10 N), where n is the number of digits

This implementation directly calculates the reversed number by multiplying the current reversed number 
by 10 and adding the last digit of the input number in each iteration. It doesn't require a separate 
modulo operation to extract the last digit because it directly operates on the input number.

The time complexity of this solution remains O(log10 n), where n is the number of digits in the input 
number. This is because the number of iterations in the loop is proportional to the number of digits 
in the input number.

Space Complexity: O(1)
"""

def reverse_number_optimal(number):
    reversed_num = 0
    while number != 0:
        # Multiply the current reversed number by 10 and add the last digit of the input number
        reversed_num = reversed_num * 10 + number % 10
        # Remove the last digit from the input number by dividing by 10
        number //= 10
    return reversed_num

# Test the function
num = 123450
reversed_num = reverse_number_optimal(num)
print("Original number:", num)
print("Reversed number:", reversed_num)