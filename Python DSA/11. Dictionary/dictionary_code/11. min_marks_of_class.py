<<<<<<< HEAD
# Print the minimum mark in that class

students = {
             "anirudh": [54, 6, 32, 5, 66],
             "sagar": [59, 87, 8, 4, -11],
             "akul": [52, 47, 85, 63, 66],
           }

min_marks = float('inf')

for  marks in students.values():
    for mark in marks:
        if  min_marks > mark:
            min_marks = mark

# Print the minimum mark in that class

students = {
             "anirudh": [54, 6, 32, 5, 66],
             "sagar": [59, 87, 8, 4, -11],
             "akul": [52, 47, 85, 63, 66],
           }

min_marks = float('inf')

for  marks in students.values():
    for mark in marks:
        if  min_marks > mark:
            min_marks = mark

>>>>>>> 23e42bfffef4fd673de480cb5d8ac70515f9550d
print("The maximum mark in the class is:", min_marks)