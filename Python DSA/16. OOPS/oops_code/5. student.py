# Better code with taking user inputs and displaying the values

class Student:
    # below are data members/attributes of the class and methods/functions that can be called on an 
    # instance of this class

    def __init__(self, roll_no: int, name: str, gender: str, age: int = 0, phone_number: int = 0):   # constructor method to initialize attributes
        self.roll_no = roll_no                 # reference variable for 'roll_no' attribute 
        self.name = name                       # reference variable for 'name' attribute
        self.gender = gender                   # reference variable for 'gender' attribute    
        self.age = age                         # reference variable for 'age' attribute
        self.phone_number = phone_number       # reference variable for 'phone_number' attribute
#   def __init__(self):  # constructor
#       print("INIT")
#       self.roll_no = int(input("Enter Roll No : "))
#       self.name = input("Enter Name : ")
#       self.gender = input("Enter Gender [M/F] : ")
#       self.age = int(input("Enter Age : "))
#       self.phone_number = int(input('Enter Phone number: ')) # global because of self
    
    def display(self): # self is the object that is being called
        print(self)
        print(f"Roll Number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone Number = {self.phone_number}")

# object of class -> this is not printable
s1 = Student(14, "Jane", "Male", 44, 9988998899)
s1.display() 

s2 = Student(name="Anirudh", age=99, gender="Male", roll_no=44, phone_number=333333)
s2.display() 