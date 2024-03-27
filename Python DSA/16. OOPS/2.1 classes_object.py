# Better code with displaying the values

class Student:
    # below are data members/attributes of the class and methods/functions that can be called on an 
    # instance of this class
    roll_no = 0
    name = ""
    gender = ""
    age = 0

    def display(self): # self is the object that is being called
        print(self)
        print(f"Roll Number = {self.roll_no}")
        print(f"Name = {self.name}")
        print(f"Gender = {self.gender}")
        print(f"Age = {self.age}")

# object of class -> this is not printable
s1 = Student()

# Accessing the variable of object S1 

s1.roll_no = 17
s1.name = "james"
s1.gender = "male"
s1.age = 24

print(s1)
s1.display()

'''

In Python, self is a reference to the current instance of a class. When you define a method within a 
class, you typically use self as the first parameter of the method. This allows you to access the 
attributes and methods of the current object within that method.

For example, consider the following Person class:
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")
'''
In this class:

-> self.name and self.age are attributes of the Person class.
-> self is used to access these attributes within the __init__ method and the introduce method.
-> When you create an instance of the Person class, self will automatically refer to that instance:
'''
person1 = Person("Alice", 25)
person1.introduce()  # Output: My name is Alice and I am 25 years old.
'''
In this example, self.name and self.age refer to the name and age attributes of the person1 instance, 
respectively.

Using self allows you to access and modify instance variables within class methods, making it a 
fundamental concept in object-oriented programming in Python.
'''