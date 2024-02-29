# Create a function findSmallest that accepts an List of Integers and returns the smallest number from
# the list.

def findSmallest(numbers):
    # Check if the list is not empty
    if not numbers:
        return None  # Return None for an empty list

    # Initialize the smallest number with the first element of the list
    smallest_number = numbers[0]

    # Iterate through the list to find the smallest number
    for num in numbers:
        if num < smallest_number:
            smallest_number = num

    return smallest_number

# Example usage
my_numbers = [34, 11, 91, 59, 33, 22]
smallest = findSmallest(my_numbers)

if smallest is not None:
    print(f"The smallest number is: {smallest}")
else:
    print("The list is empty.")