# Make a function named checkArmstrong which accepts an integer n from the user. Return True or False
# if that number is an armstrong number

def checkArmstrong(num: int) -> bool:
     # Function to calculate the number of digits in a given number
    def count_digits(num):
        count = 0
        while num > 0:
            num //= 10
            count += 1
        return count

    # Calculate the sum of digits raised to the power of the number of digits
    num_of_digits = count_digits(num)
    temp = num
    armstrong_sum = 0

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_of_digits
        temp //= 10

    # Check if the number is an Armstrong number
    return num == armstrong_sum

print(checkArmstrong(153)) # 1^3 + 5^3 + 3^3 = 153 --> True
print(checkArmstrong(407)) # 4^3 + 0^3 + 7^3 = 407 --> True
print(checkArmstrong(1234)) # 1^4 + 2^4 + 3^4 + 4^4 = 1 + 16 + 81 + 256 = 354 --> False
