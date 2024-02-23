# Reverse Digits

def reverse_digits(num):
    rev_num = 0
    rem = 0
    
    while num != 0:
        rem = num % 10  # gets the last digit of the number 
        rev_num = rev_num * 10 + rem # is updated by multiplying it by 10 and adding the remainder.
        num = num // 10 # last digit is removed from the number
    
    return rev_num

num1: int = int(input("Enter the number: "))

print("Reverse of digits", num1, " :",  reverse_digits(num1))