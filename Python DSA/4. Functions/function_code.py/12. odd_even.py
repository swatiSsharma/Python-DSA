# Check odd even using function

def checkOddEven(num: int):
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")


num: int = int(input(f"Enter a number to check whether it's Odd or Even: "))
checkOddEven(num)
checkOddEven(56)
checkOddEven(1222)