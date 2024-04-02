# Better code with taking user inputs and displaying the values

class Student:
    # below are data members/attributes of the class and methods/functions that can be called on an 
    # instance of this class
    def __init__(self) -> None:  # constructor
        print("INIT")
        self.roll_no = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.gender = input("Enter Gender [M/F] : ")
        self.age = int(input("Enter Age : "))
        self.phone_number = int(input('Enter Phone number: ')) # global because of self
    
    def updateInfo(self, new_number: int) -> None:
        self.name = input("Enter the updated name:")
        self.phone_number = new_number


    def display(self) -> None: # self is the object that is being called
        print(self)
        print(f"Roll Number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone Number = {self.phone_number}")

# object of class -> this is not printable
s1 = Student()
s1.updateInfo(9326280480)
s1.display() 