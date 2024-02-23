# Sum of digits

def sum_of_digits(number):
    digit_sum = 0

    while number > 0:
        digit_sum += number % 10 # last digit
        number //= 10 # to remove last digit
        
    return digit_sum

num1: int = int(input("Enter the number: "))

print("Sum of digits", num1, " :",  sum_of_digits(num1))