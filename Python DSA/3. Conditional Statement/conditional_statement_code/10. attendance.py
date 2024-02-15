# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
'''
Take following input from user
- Number of classes held
- Number of classes attended

1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
'''
# Get input from the user
classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

# Calculate percentage of classes attended
attendance_percentage = (classes_attended / classes_held) * 100

# Print percentage of classes attended
print(f"Percentage of classes attended: {attendance_percentage:.2f}%")

# Check if the student is allowed to sit in the exam
if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam due to low attendance.")