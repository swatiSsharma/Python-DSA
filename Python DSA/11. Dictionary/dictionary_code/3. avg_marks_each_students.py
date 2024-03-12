# Print the average marks of each students

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}

for  name, marks in students.items():
    total_marks = 0    
    for mark in marks:
        total_marks += mark
    
    avg_marks = total_marks/len(marks)
    print("The average marks of {} is {:.2f}".format(name,avg_marks))   
