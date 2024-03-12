my_dict ={
    'name':'John',
    'akul': 11,
    'muskan': 56,
    'sanjay': None # not a best way for declared with a value None
}

print(my_dict.get("abc",0))

'''
To get the value associated with a specific key in a dictionary in Python, you can use the square 
bracket notation or the get() method. Here are examples of both approaches:
'''
students = {
    "anirudh": [54, 6, 32, 5, 66],
    "sagar": [59, 87, 8, 4, 11],
    "akul": [52, 47, 85, 63, 66],
}

# Using square bracket notation
anirudh_marks = students["anirudh"]
print("Anirudh's marks:", anirudh_marks)

# Using get() method
sagar_marks = students.get("sagar")
print("Sagar's marks:", sagar_marks)
'''
Both methods will give you the list of marks associated with the specified key. The difference is 
that using square brackets directly might raise a KeyError if the key is not found, while the get() 
method allows you to provide a default value in case the key is not present:
'''
# Using get() method with a default value
akul_marks = students.get("akul", [])
print("Akul's marks:", akul_marks)
'''
In this case, if "akul" is not present in the dictionary, akul_marks will be an empty list (the 
default value specified).
'''