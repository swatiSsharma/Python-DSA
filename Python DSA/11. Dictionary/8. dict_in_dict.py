<<<<<<< HEAD
# Dictionary in Dictionary

'''
In Python, you can have dictionaries nested within other dictionaries, creating a structure commonly 
referred to as a nested or dictionary of dictionaries. Each inner dictionary serves as the value 
for a key in the outer dictionary. Here's an example:
'''

students = {
    "anirudh": {
        "math": 85,
        "science": 90,
        "english": 78
    },
    "sagar": {
        "math": 92,
        "science": 88,
        "english": 95
    },
    "akul": {
        "math": 78,
        "science": 84,
        "english": 80
    }
}

# Accessing values in the nested dictionary
print("Anirudh's math score:", students["anirudh"]["math"])
print("Sagar's english score:", students["sagar"]["english"])
print("Akul's science score:", students["akul"]["science"])

'''
In this example, each student's name is a key in the outer dictionary, and the corresponding value 
is another dictionary containing subject scores.

You can access and manipulate the nested dictionary values using multiple square brackets to navigate 
through the levels of nesting. Remember that dictionaries are mutable, so you can add, modify, or 
remove values dynamically.
'''
# Adding a new student and their scores:
students["john"] = {
    "math": 88,
    "science": 76,
    "english": 89
}

# Modifying a student's score:

students["sagar"]["english"] = 97

'''
These operations allow you to create and manipulate complex data structures to represent more 
detailed information about each student.
=======
# Dictionary in Dictionary

'''
In Python, you can have dictionaries nested within other dictionaries, creating a structure commonly 
referred to as a nested or dictionary of dictionaries. Each inner dictionary serves as the value 
for a key in the outer dictionary. Here's an example:
'''

students = {
    "anirudh": {
        "math": 85,
        "science": 90,
        "english": 78
    },
    "sagar": {
        "math": 92,
        "science": 88,
        "english": 95
    },
    "akul": {
        "math": 78,
        "science": 84,
        "english": 80
    }
}

# Accessing values in the nested dictionary
print("Anirudh's math score:", students["anirudh"]["math"])
print("Sagar's english score:", students["sagar"]["english"])
print("Akul's science score:", students["akul"]["science"])

'''
In this example, each student's name is a key in the outer dictionary, and the corresponding value 
is another dictionary containing subject scores.

You can access and manipulate the nested dictionary values using multiple square brackets to navigate 
through the levels of nesting. Remember that dictionaries are mutable, so you can add, modify, or 
remove values dynamically.
'''
# Adding a new student and their scores:
students["john"] = {
    "math": 88,
    "science": 76,
    "english": 89
}

# Modifying a student's score:

students["sagar"]["english"] = 97

'''
These operations allow you to create and manipulate complex data structures to represent more 
detailed information about each student.
>>>>>>> 23e42bfffef4fd673de480cb5d8ac70515f9550d
'''