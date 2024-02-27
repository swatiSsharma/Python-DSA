# Make a function named sumOfFirstAndLastDigit which accepts an integer n from the user. Calculate 
# the sum of first and last digit of a number and return it

def sumOfFirstAndLastDigit(num: int) -> int:
    if len(str(num)) == 1:
        return num
    else:
        
        # Extract the last digit
        last_digit = num % 10

        # Extract the first digit
        first_digit = 0
        while num > 0:
            first_digit = num % 10
            num //= 10

        # Calculate and return the sum of the first and last digits
        return first_digit + last_digit

print(sumOfFirstAndLastDigit(1234)) # 5
print(sumOfFirstAndLastDigit(8471)) # 9
print(sumOfFirstAndLastDigit(5)) # 5
print(sumOfFirstAndLastDigit(99)) # 18