# Take Salary as input from User and Update the salary of an employee
'''
- salary between 10,000 and 20, 000, 10 % increment
- salary between 20,000 and 50,000, 15 % increment
- salary more than 50,000, 20 % increment
- salary less than 10,000, 5 % increment
'''

# Get input from the user for salary
salary: float = float(input("Enter the current salary of the employee: "))

# Update the salary based on conditions
if salary < 10000:
    increment_percentage = 5
elif 10000 <= salary < 20000:
    increment_percentage = 10
elif 20000 <= salary < 50000:
    increment_percentage = 15
else:
    increment_percentage = 20

# Calculate the increment amount and update the salary
increment_amount = (increment_percentage / 100) * salary
updated_salary = salary + increment_amount

# Print the increment percentage and updated salary
print(f"Increment percentage: {increment_percentage}%")
print(f"Updated salary: Rs. {updated_salary:.2f}")