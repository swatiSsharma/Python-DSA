
my_details = [{"name": "Swati", "age": 67, "gender": "Female"},
              {"name": "Clara", "age": 52, "gender": "Female"},
              {"name": "Eric", "age": 58, "gender": "Male"},
              {"name": "John", "age": 66, "gender": "Male"},
             ]

print(len(my_details))

# Sort the list using age -> Using sort
my_details.sort(key=lambda x:x['age'], reverse=True)
print("Sorted List by Age using sort : ",my_details)
print()

my_details = [{"name": "Swati", "age": 67, "gender": "Female"},
              {"name": "Clara", "age": 52, "gender": "Female"},
              {"name": "Eric", "age": 58, "gender": "Male"},
              {"name": "John", "age": 66, "gender": "Male"},
             ]
# Sort the list using age -> Sorted
sorted_list = sorted(my_details, key=lambda x:x['age'])
print("Sorted List by Age using sorted : ", sorted_list)
print()
## Alternate way

def func_sort(x):
    return x["age"]

my_details.sort(key=func_sort, reverse=True) 
'''We dont call the function just reference it'''

my_details = [{"name": "Swati", "age": 67, "gender": "Female"},
              {"name": "Clara", "age": 52, "gender": "Female"},
              {"name": "Eric", "age": 58, "gender": "Male"},
              {"name": "John", "age": 66, "gender": "Male"},
             ]

print(len(my_details))

# Sort the list using age -> Using sort
my_details.sort(key=lambda x:x['age'], reverse=True)
print("Sorted List by Age using sort : ",my_details)
print()

my_details = [{"name": "Swati", "age": 67, "gender": "Female"},
              {"name": "Clara", "age": 52, "gender": "Female"},
              {"name": "Eric", "age": 58, "gender": "Male"},
              {"name": "John", "age": 66, "gender": "Male"},
             ]
# Sort the list using age -> Sorted
sorted_list = sorted(my_details, key=lambda x:x['age'])
print("Sorted List by Age using sorted : ", sorted_list)
print()
## Alternate way

def func_sort(x):
    return x["age"]

my_details.sort(key=func_sort, reverse=True) 
'''We dont call the function just reference it'''
print("Alternate Way - Sorted List by Age : ", my_details)