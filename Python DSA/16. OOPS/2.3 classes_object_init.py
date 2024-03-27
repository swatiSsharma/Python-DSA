# Better code with taking user inputs and displaying the values

class Student:
    # below are data members/attributes of the class and methods/functions that can be called on an 
    # instance of this class
    def __init__(self):  # constructor
        print("INIT")
        self.roll_no = int(input("Enter Roll No : "))
        self.name = input("Enter Name : ")
        self.gender = input("Enter Gender [M/F] : ")
        self.age = int(input("Enter Age : "))
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
s1.display() 

'''
The __init__ method in Python is a special method used for initializing newly created objects. It is 
also known as the constructor method. When you create a new instance of a class, the __init__ method 
is automatically called to initialize the object's attributes.

this can be used in scenarios where  we want some default value or behavior when creating instances, 
something that is used manadatory.

In object-oriented programming, a constructor is a special method used for initializing newly created 
objects. It is called automatically when a new instance of a class is created. The constructor method 
typically initializes the object's attributes or performs other setup tasks needed for the object to 
be in a valid state.

In Python, the constructor method is defined using the __init__ method. When you create a new instance 
of a class, Python automatically calls the __init__ method for that class.
It does not allocate memory, but is a sort of constructor
'''