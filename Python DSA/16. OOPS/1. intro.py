# Object oriented programming

'''
"OOPS" usually refers to Object-Oriented Programming (OOP). Object-Oriented Programming is a 
programming paradigm that revolves around the concept of objects, which can contain data (attributes) 
and code (methods). Python is an object-oriented programming language, and it supports classes, 
objects, inheritance, polymorphism, and encapsulation.

Here's a brief overview of some key OOP concepts in Python:

-> Class: A generalised blueprint for creating objects. It defines the attributes and methods that the
          objects will have.
          It is used to minimise redundancy and increase code reuseability

-> Object: An instance of a class. It contains data (attributes) and behavior (methods) defined by its 
           class.

-> Inheritance: The mechanism by which a class can inherit attributes and methods from another class. 
                It promotes code reusability and allows for the creation of specialized classes based 
                on existing ones.

-> Encapsulation: The bundling of data (attributes) and methods that operate on that data into a 
                  single unit (class). It helps in hiding the internal state of an object and only 
                  exposing necessary functionality through methods.

-> Polymorphism: The ability of different classes to be treated as instances of the same class through
                 a common interface. It allows for flexibility and dynamic behavior in code.


'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return "Woof!"

# Creating an object of the Dog class
my_dog = Dog("Buddy", 5)

# Accessing attributes and calling methods
print(my_dog.name)   # Output: Buddy
print(my_dog.age)    # Output: 5
print(my_dog.bark()) # Output: Woof!
