<<<<<<< HEAD
'''
Create a python function named isPalindrome which accepts a string
as a parameter and return True if its a palindrome. Palindrome are words
which is same when read from start and same when read from the end
'''

def isPalindrome(string: str) -> bool:
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

print(isPalindrome("moom")) # True
print(isPalindrome("ABCcba"))  # True
print(isPalindrome("ABCcbaa")) # False
=======
'''
Create a python function named isPalindrome which accepts a string
as a parameter and return True if its a palindrome. Palindrome are words
which is same when read from start and same when read from the end
'''

def isPalindrome(string: str) -> bool:
    if string.lower() == string[::-1].lower():
        return True
    else:
        return False

print(isPalindrome("moom")) 
print(isPalindrome("ABCcba"))
print(isPalindrome("ABCcbaa"))
>>>>>>> 5dc3bcbce5040aceb221c751b330de1970861a6d
