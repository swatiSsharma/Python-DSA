'''
Write a program that takes a character as input and prints 1, 0, or -1 according to the following rules.

1, if the character is an uppercase alphabet (A - Z).
0, if the character is a lowercase alphabet (a - z).
-1, if the character is not an alphabet.

Example:
Input: The character is 'a'.

Output: 0

Explanation: The input character is lowercase, so our answer is 0.
'''

# Variation 1

def firstCharacterCase(userInput: str) -> int:
## METHOD 1
##   ch = input()
##   if ch >= 'A' and ch <= 'Z' :
##       print(1)
##   elif ch >= 'a' and ch <= 'z' :
##       print(0)
##   else :
##       print(-1)
    
    # Method 2
    if 'a' <= userInput <= 'z':
        return 0
    elif 'A' <= userInput <= 'Z':
        return 1
    else:
        return -1
    
    
    
print(firstCharacterCase('a'))   # Output:   0
print(firstCharacterCase('V'))   # Output:   1
print(firstCharacterCase('3'))   # Output:  -1
print(firstCharacterCase('#'))   # Output:  -1