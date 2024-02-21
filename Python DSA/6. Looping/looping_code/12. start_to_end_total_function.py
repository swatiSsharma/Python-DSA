# Create function for Total sum from start to end

def sumTotal(start: int, end: int) -> int:
    total: int = 0
    i: int = start

    while i <= end:
        total += i
        i += 1
    
    print(f"The sum of numbers from {start} and {end} is: {total}".format(start, end, total))

start: int= int(input("Enter Start value: "))
end: int= int(input("Enter End value: "))

sumTotal(start, end)