'''
Check whether a given number ’n’ is a palindrome number.

Note :
Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.
Example:
Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415.
'''

num: int = 121#int(input('Enter the number: '))
revNum = 0
while num  > 0:
    digit = num % 10
    num = num // 10
    revNum = revNum * 10 + digit

if revNum == num:
    print("Yes")
else:
    print("No")
    