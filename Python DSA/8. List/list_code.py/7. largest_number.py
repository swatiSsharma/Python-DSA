# Create a function findLargest that accepts an List of Integers and returns the largest number from
# the list.

def findLargest(numbers):
    # Check if the list is not empty
    if not numbers:
        return None  # Return None for an empty list

    # Initialize the largest number with the first element of the list
    largest_number = numbers[0]

    # Iterate through the list to find the largest number
    for num in numbers:
        if num > largest_number:
            largest_number = num

    return largest_number

my_numbers = [34, 11, 91, 59, 33, 22]
largest = findLargest(my_numbers)

if largest is not None:
    print(f"The largest number is: {largest}")
else:
    print("The list is empty.")