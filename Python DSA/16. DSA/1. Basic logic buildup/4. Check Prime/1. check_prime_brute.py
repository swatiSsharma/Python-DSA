# Brute Force solution for Check prime
'''
The brute force approach involves checking divisibility of 'n' by every integer from 2 to 'n-1'.
'''
"""
Time Complexity: O(N)

Space Complexity: O(1)
"""

def is_prime_brute(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
