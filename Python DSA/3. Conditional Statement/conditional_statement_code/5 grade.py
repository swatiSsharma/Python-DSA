# Grade

## Variation 1
'''
Ask a mark from user between 1 to 100
91-100 --> A
81-90 --> B
71-80 --> C
61-70 --> D
0-60 --> Fail
''' 
mark: int = int(input("Enter a mark between 1 to 100: "))

if 91 <= mark <= 100:
    grade = "A"
elif 81 <= mark <= 90:
    grade = "B"
elif 71 <= mark <= 80:
    grade = "C"
elif 61 <= mark <= 70:
    grade = "D"
elif 0 <= mark <= 60:
    grade = "Fail"
else:
    grade = "Invalid input. Please enter a mark between 1 to 100."

print(f"Grade: {grade}")


## Variation 2
# Get input from the user
score = float(input("Enter the student's score: "))

# Determine the corresponding grade
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = "Invalid input. Please enter a score between 1 to 100."

# Print the corresponding grade
print(f"The student's grade is: {grade}")