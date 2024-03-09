"""
Given an integer n, find if n is positive, negative or 0.

If n is positive, print "Positive"

If n is negative, print "Negative"

And if n is equal to 0, print "Zero".
"""

def checkNumber(num: int) -> str:
    if  num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"   
    else:   
        return "Zero"
    
print(checkNumber(-5)) # Negative
print(checkNumber(5)) # Postive
print(checkNumber(0))  # Zero