
"""
Time Complexity: O(log10 N), where n is the number of digits

The time complexity of this solution is O(log n), where n is the number of digits in the input number.
This is because the loop iterates through each digit of the number, and the number of iterations is 
proportional to the number of digits in the input number. Additionally, there is no extra overhead of 
converting the number to a string or reversing a string, making this solution more efficient.

Space Complexity: O(1)

"""

def reverse_number(number):
    reversed_num = 0
    while number != 0:
        # Extract the last digit
        digit = number % 10
        # Append the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the original number
        number //= 10
    return reversed_num

# Test the function
num = 123450
reversed_num = reverse_number(num)
print("Original number:", num)
print("Reversed number:", reversed_num)