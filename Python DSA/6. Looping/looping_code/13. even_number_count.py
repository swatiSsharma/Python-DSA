# How many Even Numbers are there from 1 to 100

start_number: int = 1
end_number: int = 100
current_number = start_number

if start_number % 2 != 0:
    current_number += 1

even_count = 0

while current_number <= end_number:
    even_count += 1
    current_number += 2  

print(f"The count of even numbers between {start_number} and {end_number} is: {even_count}")
