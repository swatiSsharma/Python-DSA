def totalMarks(physics: int, chemistry: int, english: int, computer: int, maths: int):
    print(f"{physics }")
    print(f"{chemistry }")    
    print(f"{english }")
    print(f"{computer }")
    print(f"{maths  }")

    total = physics + chemistry + english + computer + maths
    return  total

result =  totalMarks(85,76,90,72,83)
print("Total Marks are : ", result)

result =  totalMarks(english = 85,maths = 76, computer = 90, physics = 72, chemistry = 83)
print("Total Marks are : ", result)

# order should be left to right incase we dont name the parameter
result =  totalMarks(72, 84, english = 85,maths = 76, computer = 90)
print("Total Marks are : ", result)

