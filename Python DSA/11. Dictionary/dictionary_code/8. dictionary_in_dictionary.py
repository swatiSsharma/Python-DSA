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
        print(f"{name} has no age")