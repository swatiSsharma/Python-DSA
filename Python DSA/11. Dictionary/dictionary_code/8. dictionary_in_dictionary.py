<<<<<<< HEAD
# Using a dictionary print Age in dictionary

"""
anirudh has age = 66
sanjay has age = 11
"""
students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"age": 11, "gender": "Male"},
    "vandana": {"age": 53, "gender": "Female"},
}

for name, details in students.items():
    print(f"{name.title()} has age = {details['age']}") 
    

""" Secondcase scenario where age key is missing"""
students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"gender": "Male"},
    "vandana": {"age": 53, "gender": "Female"},
}
for name, details in students.items():
    if "age" in details.keys():
        print(f"{name} has age = {details['age']}")
    else:
=======
# Using a dictionary print Age in dictionary

"""
anirudh has age = 66
sanjay has age = 11
"""
students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"age": 11, "gender": "Male"},
    "vandana": {"age": 53, "gender": "Female"},
}

for name, details in students.items():
    print(f"{name.title()} has age = {details['age']}") 
    

""" Secondcase scenario where age key is missing"""
students = {
    "anirudh": {"age": 66, "gender": "Male"},
    "sanjay": {"gender": "Male"},
    "vandana": {"age": 53, "gender": "Female"},
}
for name, details in students.items():
    if "age" in details.keys():
        print(f"{name} has age = {details['age']}")
    else:
>>>>>>> 23e42bfffef4fd673de480cb5d8ac70515f9550d
        print(f"{name} has no age")