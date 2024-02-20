# Write a Python program that takes four numbers from the user.
# Implement a function to find the average of the first three numbers. Then,
# create another function to check if the average is greater than or equal to
# the fourth number. Make sure to use these two functions to determine and
# print whether the average is greater than or equal to the fourth number or
# not.

def calculateAverage(num1: int, num2: int, num3: int):
    return  (num1 + num2 + num3)/3

def compareAverageAndFourthNumber(avg: float, num4):
    return avg >= num4

if __name__ == "__main__":
    num1: int = int(input("Enter first number: "))
    num2: int = int(input("Enter second number: "))
    num3: int = int(input("Enter third number: "))
    num4: int = int(input("Enter forth number: "))

    result = compareAverageAndFourthNumber(calculateAverage(num1, num2, num3), num4)

    if result:
        print(f"The average ({calculateAverage(num1, num2, num3)}) is greater than or equal to {num4}.")
    else:
        print(f"The average ({calculateAverage(num1, num2, num3)}) is less than {num4}.")
