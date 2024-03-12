'''
using a dictionary sum up all the values in list

anirudh has scored 432 marks
sagar has scored 412 marks

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}
'''
students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}
print("\nUsing sum function\n")

for i in  students:
    print(i,"has scored",sum(students[i]),"marks")


print("\nWithout using sum function\n")
# total_marks = 0 this will result in cummulative marks
'''
anirudh has scored 163 marks
sagar has scored 332 marks
akul has scored 645 marks
'''
for student, scores in students.items():
    total_marks = 0    
    for score in scores:
        total_marks += score

    print(f"{student} has scored {total_marks} marks")