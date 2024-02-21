# Create a function for Total sum from 1 to 10

def sumTotal() -> int:
    i: int = 1
    total: int = 0
    while i <= 10:
        total += i
        i += 1
    
    print("The sum of numbers from 1 to 10 is:", total)

sumTotal()

