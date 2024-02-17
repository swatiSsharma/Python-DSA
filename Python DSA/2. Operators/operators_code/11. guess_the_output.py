'''
There are two variables.
a=5 b=10 What will be the output of following:

a > 5 and b >= 10
a >= 5 or not b > 10
not ( a > 5 and b > 5)
not ( a < 10 or not b < 10)
not ( not a <= 5 or not b >= 10)
'''
a = 5
b = 10
print(a > 5 and b >= 10) # False

'''
a > 5 and b >= 10 a is 5, which is not greater than 5. So, the first part (a > 5) is False. 
b is 10, which is equal to 10. So, the second part (b >= 10) is True. The overall expression is False
(False and True).
'''

print(a >= 5 or not b > 10) # True

'''
a >= 5 or not b > 10 a is 5, which is equal to 5. So, the first part (a >= 5) is True. b is 10, 
which is greater than 10. So, the second part (not b > 10) is False. The overall expression is True
 (True or False).
'''

print(not ( a > 5 and b > 5)) # True

'''
not ( a > 5 and b > 5) a is 5, which is not greater than 5. So, the first part (a > 5) is False. 
b is 10, which is greater than 5. So, the second part (b > 5) is True. The expression inside the 
parentheses is False (False and True), and the not negates it, resulting in True.
'''

print(not ( a < 10 or not b < 10)) # False

'''
not ( a < 10 or not b < 10) a is 5, which is less than 10. So, the first part (a < 10) is True. b is
10, which is not less than 10. So, the second part (not b < 10) is False. The expression inside the 
parentheses is True (True or False), and the not negates it, resulting in False.
'''

print(not ( not a <= 5 or not b >= 10)) # True

'''
not ( not a <= 5 or not b >= 10) a is 5, which is equal to 5. So, the first part (not a <= 5) is False.
b is 10, which is greater than 10. So, the second part (not b >= 10) is False. The expression inside 
the parentheses is False (False or False), and the not negates it, resulting in True.
'''