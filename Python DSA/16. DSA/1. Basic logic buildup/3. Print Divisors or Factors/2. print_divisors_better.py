"""
Time Complexity: O(√n)

1) Iterating from 2 to the square root of the number: This step takes O(√n) time because it 
   iterates at most up to the square root of the given number.
2) Checking divisibility and adding factors to the list: For each iteration, checking divisibility and 
   adding factors to the list takes constant time.
3) Sorting the factors: After collecting all factors, sorting them takes 
   O(√n log(√n))=(√n log N) time.
4) Joining and printing the factors: This step also takes O(√n) time as it involves iterating over
   all the factors to join them into a string.

Since the most significant term in the time complexity is O(√n log N), log N is less significant 
compared to √n, when n is large, the overall time complexity can be simplified to O(√n). This 
is because the time taken to iterate and find factors dominates the overall time complexity.

Space  Complexity: O(2 * √n) = O(√n)
"""

import math

def print_factors(number):
    # Initialize a list to store factors
    factors = []
    
    # Add 1 and the number itself as factors
    factors.append(1)
    
    # Iterate from 2 to the square root of the number
    sqrt_num = math.isqrt(number)
    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            factors.append(i)
            # If i is not equal to number // i, then add number // i as well
            if i != number // i:
                factors.append(number // i)

    # Add the number itself if it's not 1
    if number != 1:
        factors.append(number)

    # Print factors in one line
    print("Factors of", number, "are:", ", ".join(map(str, sorted(factors))))

# Test the function
number = 36
print_factors(number)
print()
number = 39
print_factors(number)