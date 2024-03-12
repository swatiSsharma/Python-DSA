# Print the max and min marks of every student

def  print_max_min(students):
    for name in students.keys():
        grades = students[name]
        print("For {} : Max Marks is {}, Min Marks is {}".format(name, max(grades), min(grades)))

students = {
             "anirudh": [54, 6, 32, 5, 66],
             "sagar": [59, 87, 8, 4, 11],
             "akul": [52, 47, 85, 63, 66],
           }

print_max_min(students) 