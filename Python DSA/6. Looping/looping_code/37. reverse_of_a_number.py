'''
Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 
       will be 401 instead of 00401.
'''

def revNum(num: int) -> int:
    num = str(num)
    num = num.strip('0')
    temp = int(num)
    revNum = 0

    while temp > 0:
        lastDigit = temp % 10
        temp = temp // 10
        revNum = revNum * 10  + lastDigit

    return revNum

print(revNum(1234))  # 4321
print(revNum(14008)) # 80041
print(revNum(956700000)) # 7659
print(revNum(10400)) #401