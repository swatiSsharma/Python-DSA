# Bad code

class Student:
    roll_no = 0
    name = ""
    gender = ""
    age = 0

# object of class  
s1 = Student()
print(s1) # this gives the object  id <__main__.Student at location>

# Accessing the variable of object S1 

# prints value of the class
print(s1.name)
print(s1.roll_no)
print(s1.gender)
print(s1.roll_no)

# prints value of the assignment as above
roll_no = 17
name = "james"
gender = "male"
age = 24

print(s1.name)
print(s1.roll_no)
print(s1.gender)
print(s1.roll_no)