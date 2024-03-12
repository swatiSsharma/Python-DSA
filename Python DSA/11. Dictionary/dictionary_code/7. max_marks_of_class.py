# Print the maximum mark in that class

students = {
             "anirudh": [54, 6, 32, 5, 66],
             "sagar": [59, 87, 8, 4, 11],
             "akul": [52, 47, 85, 63, 66],
           }

max_marks = 0

for  marks in students.values():
    for mark in marks:
        if  max_marks < mark:
            max_marks = mark

print("The maximum mark in the class is:", max_marks)