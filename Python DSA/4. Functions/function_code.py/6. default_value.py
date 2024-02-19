# Default Value

def totalMarks(
    physics: int, chemistry: int, maths: int, english: int = 0, computer: int = 0
):
    print(f"{physics = }")
    print(f"{chemistry = }")
    print(f"{maths = }")
    print(f"{english = }")
    print(f"{computer = }")
    total = physics + chemistry + maths + english + computer
    print(f"Total marks = {total}")

# totalMarks(english=54, physics=23, chemistry=78, computer=100, maths=78)
# totalMarks(59, 100, english=34, computer=11, maths=98)
totalMarks(45, 55, 85, computer=100)

# here in the above egs, physics: int, chemistry: int, maths: int are mandatory  arguments.

def user_info (name: str, gender: str, age: int = 26):
    print(f"{name }")
    print(f"{age }")
    print(f"{gender }")    
    print(f"Hello, {name}! You are {age} years old and you are a {gender}.")

# order should be left to right incase we dont name the parameter
user_info("hina", gender = "female", age = 21)
user_info(name="Ali", age=16, gender="male")
user_info(name = "karan",gender="male")
