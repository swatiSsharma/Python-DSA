# Create function to find how many Even Numbers are there from 1 to 100

def count_even_numbers(start, end):
    if start % 2 != 0:
        start += 1

    even_count = 0
    current_number = start

    while current_number <= end:
        even_count += 1
        current_number += 2  # Increment by 2 to stay on even numbers

    return even_count

# Get user input for the range
start_number = int(input("Enter the starting number: "))
end_number = int(input("Enter the ending number: "))

result = count_even_numbers(start_number, end_number)
print(f"The count of even numbers between {start_number} and {end_number} is: {result}")
