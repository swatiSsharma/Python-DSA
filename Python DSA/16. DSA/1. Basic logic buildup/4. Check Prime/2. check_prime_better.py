# Better solution for Checking prime number
'''
hecking divisibility of 'n' by integers from 2 to √n. This is because if 'n' is divisible by any 
number larger than √n, it must also be divisible by a factor smaller than √n.
'''
"""
Time Complexity: O(√n)

Space Complexity: O(1)
"""

def is_prime_better(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True