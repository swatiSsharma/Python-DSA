# Take Salary as input from User and Update the salary of an employee
'''
- salary between 10,000 and 20, 000, 10 % increment
- salary between 20,000 and 50,000, 15 % increment
- salary more than 50,000, 20 % increment
- salary less than 10,000, 5 % increment
'''

def incrementSalary(original_salary: float):
    if original_salary < 10000:
        increment_percentage = 5
    elif 10000 <= original_salary < 20000:
        increment_percentage = 10
    elif 20000 <= original_salary < 50000:
        increment_percentage = 15
    else:
        increment_percentage = 20

    increment_amount: float = original_salary * increment_percentage / 100
    updated_salary: float = original_salary + increment_amount

    print(f"The original salary was Rs.{original_salary:.2f}")
    print(f"The increment percentage is {increment_percentage}%")
    print(f"The updated salary is Rs.{updated_salary}")


incrementSalary(60000)