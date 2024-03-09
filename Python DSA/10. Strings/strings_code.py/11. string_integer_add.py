# Take string input from user and check if both are integers then give sum as ouptut 
# otherwise concatenate the strings


def concatAdd(str1: str, str2: str):
    if a.isdigit() and b.isdigit():
        print(int(a)+int(b))
    else:
        print(a+b)

a: str = input("Enter a string: ")
b: str = input("Enter a string: ")
concatAdd(a, b)
concatAdd('Python', "good")
concatAdd(11, 22)
concatAdd("hello", 22)