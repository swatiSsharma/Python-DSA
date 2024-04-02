# Brute force for printing divisors
"""
Time Complexity: O(N)
Space Complexity: O(K), where K is the number of factors
"""

def factors(num) -> list:
    result = []
    for i in range(1, num+1):
        if  num % i == 0 and i != num:
            result.append(i)
    return sorted(result)

# Testing the function
print(factors(28)) # [1, 2, 4,  7, 14] 