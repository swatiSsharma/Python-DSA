
def greet(name: str, age: int, gender: str):  

    # these are stored in memory at different location
    name, age, gender = '' , 0, ''
    print(f"My name is {name}, My age is {age} , My gender is {gender}", end = '\n')


# these are stored in memory at different location even if there names are like mentioned in function
a, b, c = "Hiba", 25, "Female"
greet(a, b, c)
print(a, b, c)