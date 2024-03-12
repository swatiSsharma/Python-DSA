<<<<<<< HEAD
# Print the total marks of the class

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}

total_marks = 0
for mark in students.values():
    total_marks += sum(mark)

=======
# Print the total marks of the class

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}

total_marks = 0
for mark in students.values():
    total_marks += sum(mark)

>>>>>>> 23e42bfffef4fd673de480cb5d8ac70515f9550d
print("Total Marks:", total_marks)