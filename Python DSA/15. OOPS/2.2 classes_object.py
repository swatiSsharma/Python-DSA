# Better code with taking user inputs and displaying the values

class Student:
    # below are data members/attributes of the class and methods/functions that can be called on an 
    # instance of this class
    roll_no = 0
    name = ""
    gender = ""
    age = 0
    
    # here we are overriding the values
    def setInfo(self):
        self.roll_no = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.gender = input("Enter Gender [M/F] : ")
        self.age = int(input("Enter Age : "))
        phoneNumber = int(input('Enter Phone number: ')) # local to class can't be accessed outside or print
        self.phone_number = int(input('Enter Phone number: ')) # global because of self
    
    def display(self): # self is the object that is being called
        print(self)
        print(f"Roll Number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")
        print(f"Phone Number = {self.phone_number}")

# object of class -> this is not printable
s1 = Student()
# s1.display() --> Attribute error -> incase it is called before value getting assigned using setinfo 
#                                    method
s1.setInfo()
s1.display() 