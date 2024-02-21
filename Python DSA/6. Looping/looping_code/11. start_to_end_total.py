# Print Total sum from start to end

start: int = int(input("Enter Start value: "))
end: int = int(input("Enter End value: "))

total: int = 0
i: int = start

while i <= end:
    total += i
    i += 1

print(f"The sum of numbers from {start} and {end} is: {total}".format(start, end, total))