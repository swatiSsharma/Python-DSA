# Student Class
'''
In this example:

- The Student class has three attributes: name, age, and grade.
- The __init__() method is the constructor method, which initializes the object with the provided 
  values.
- The display_info() method displays the student's information.
- The promote() method increments the student's grade by one.
'''

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def promote(self):
        self.grade += 1
        print(f"{self.name} has been promoted to grade {self.grade}")

# Example usage:
student1 = Student("Alice", 15, 9)
student1.display_info()  # Output: Name: Alice, Age: 15, Grade: 9

student1.promote()  # Output: Alice has been promoted to grade 10
student1.display_info()  # Output: Name: Alice, Age: 15, Grade: 10
