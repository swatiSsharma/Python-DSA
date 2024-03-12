# Print the average marks scored by whole class

students = {
             "anirudh": [54, 6, 32, 5, 66],
             "sagar": [59, 87, 8, 4, 11],
             "akul": [52, 47, 85, 63, 66],
           }
total_marks = 0
total_students = 0

for student, marks in students.items():
    total_marks += sum(marks)
    total_students += len(marks)

avg_marks = total_marks / total_students
print("The average marks of the class are {:.2f}".format(avg_marks))