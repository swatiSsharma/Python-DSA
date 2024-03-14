
'''
Sort the dictionary on the bases of total marks
'''

students = {
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
}

# Sorting based on total marks
sorted_students = sorted(students.items(), key=lambda x: sum(x[1]['marks']), reverse=True)
print(sorted_students)
print("Students sorted by Total Marks : ")     
for student in sorted_students:
    print(student[0],sum(student[1]['marks']))

'''
Sort the dictionary on the bases of total marks
'''

students = {
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
}

# Sorting based on total marks
sorted_students = sorted(students.items(), key=lambda x: sum(x[1]['marks']), reverse=True)
print(sorted_students)
print("Students sorted by Total Marks : ")     
for student in sorted_students:
    print(student[0],sum(student[1]['marks']))