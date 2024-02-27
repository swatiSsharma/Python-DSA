# Make a function named checkPalindrome which accepts an integer n from the user. Return True or False
# if the number is palindrome or not. Palindrome means which is same as forward and backwards. Do not 
# use STRINGS

def checkPalindrome(num: int) -> bool:
    original_number = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num = num // 10

    return original_number == reversed_num

print(checkPalindrome(91)) # False
print(checkPalindrome(1221)) # True
print(checkPalindrome(9854)) # False
print(checkPalindrome(123454321)) # True