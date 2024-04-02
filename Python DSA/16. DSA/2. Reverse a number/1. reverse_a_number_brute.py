# Brute force for reversing a number
"""
Time Complexity: O(N)
reverse a list -> (N) since we are reversing the complete list
str conversion from int -> O(N)
int conversion from str -> O(N)
Therefore, overall complexity is O(N) + O(N) + O(N) = O(3*N) which is similar to O(N)

Space  Complexity: O(1)
"""

def reverse_number_brute(number):
    # Convert the number to a string
    number_str = str(number)
    # Reverse the string
    reversed_str = number_str[::-1]
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    return reversed_number

# Test the function
num = 12345
reversed_num = reverse_number_brute(num)
print("Original number:", num)
print("Reversed number:", reversed_num)