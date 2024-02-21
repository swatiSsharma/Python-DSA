# Create a function named printPattern that takes one integer (num) as an argument. Print from -num 
# to num. Also keep in mind number passed as an argument can be negative or positive.

def printPattern(num: int):

    start = -num
    end = num
    while start <= num:
        print(start, end =" ")
        start += 1
    print()

num = 5
if num >= 0:
    printPattern(num)
else:
    printPattern(abs(num))
    
num = -9
if num >= 0:
    printPattern(num)
else:
    printPattern(abs(num))