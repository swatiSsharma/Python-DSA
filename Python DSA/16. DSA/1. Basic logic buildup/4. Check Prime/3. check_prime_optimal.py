# Optimal solution for checking prime number - The Sieve of Eratosthenes

'''
The Sieve of Eratosthenes is an ancient algorithm used to find all prime numbers up to a specified 
integer 'n'. It works by iteratively marking the multiples of each prime number starting from 2, 
thereby eliminating composite numbers and leaving only the prime numbers.

Here's the step-by-step process of the Sieve of Eratosthenes algorithm:

1) Create a boolean array (or list) sieve of size n+1, initialized with True. This array will be used 
   to mark numbers as prime or composite.
2) Mark sieve[0] and sieve[1] as False, as 0 and 1 are not prime numbers.
3) Iterate over each number i from 2 to the square root of n:
   1) If sieve[i] is True (indicating that i is prime), mark all multiples of i as False in the array 
      sieve, starting from i*i up to n, with a step size of i. This is because numbers smaller than 
      i*i that are multiples of i would already have been marked by a smaller prime factor.
4) After the loop, the indices of the array sieve that are marked as True represent prime numbers.
'''

"""
Time Complexity: O(n log log n)

Space Complexity: O(n)
"""

def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # Mark multiples of i as False
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    return sieve

'''
This function returns a boolean array sieve, where sieve[i] is True if i is a prime number and False 
otherwise. The range of numbers considered is from 0 to n, inclusive.

Once you have the sieve, you can determine if a number is prime by simply checking sieve[number]. If 
it's True, the number is prime; if it's False, the number is composite.
'''