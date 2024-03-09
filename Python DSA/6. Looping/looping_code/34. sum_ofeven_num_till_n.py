# Given a number N, print sum of all even numbers from 1 to N.

endNum: int = int(input("Enter the number: "))
startNum: int = 1
sumEvenNums: int = 0

while startNum <= endNum:
    if startNum % 2 ==  0:
        sumEvenNums += startNum
    startNum += 1
    
print("The sum of all even numbers from 1 to", endNum,"is: ", sumEvenNums)