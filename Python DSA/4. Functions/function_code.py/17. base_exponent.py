# Implement a function that takes two parameters, base and exponent, and returns the result of raising
# the base to the power of the exponent.

def baseExponent(base: int, exponent: int) -> int:
    return base ** exponent


base: int = int(input("Enter the base: "))
exponent: int = int(input("Enter the exponent: "))

print(baseExponent(base, exponent))