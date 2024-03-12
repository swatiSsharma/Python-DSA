# Print as below
"""
Q1
anirudh has scored 432 marks
sanjay has scored 112 marks
Q2
anirudh has scored 87.44%
sanjay has scored 55.22%
"""

# subjects = ["physics", "maths", "english"]
# marks_sum = sum(student[subject] for subject in subjects) / len(subjects) 
# average_marks = marks_sum / len(students)  

students = {
    "anirudh": {"physics": 54, "maths": 11, "english": 99},
    "sanjay": {"physics": 13, "maths": 40, "english": 62},
    "vandana": {"physics": 65, "maths": 85, "english": 94},
}

# Q1: Total Marks
print("Q1")
for student, scores in students.items():
    total_marks = sum(scores.values()) 
    # total_marks = scores["physics"] + scores["maths"] + scores["english"] incase the key is missing then we can use this
    '''
    for m in scores.values():
        total_marks += m
    '''
    print(f"{student} has scored {total_marks} marks")

# Q2: Average Percentage
print("\nQ2")
for student, scores in students.items():
    total_marks = sum(scores.values())
    total_subjects = len(scores)
    average_percentage = (total_marks / (total_subjects * 100)) * 100
    print(f"{student} has scored {average_percentage:.2f}%") 


