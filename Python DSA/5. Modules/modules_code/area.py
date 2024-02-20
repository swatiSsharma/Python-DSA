def circle(radius: float) -> float:
    return 3.14 * radius ** 2

def rectangle(length: float, breadth: float) -> None:
    print(length * breadth)

def triangle(base: float, height: float) -> float:
    return 0.5 * base * height

def square(side: float) -> float:
    return side ** 2


# avoid this running on the python script where this file is imported
# the __name__ is an inbulit function that contains the name of the module/script being run when only
# this file is executed
if __name__ == "__main__":
    print(square(56))
    rectangle(8, 7)