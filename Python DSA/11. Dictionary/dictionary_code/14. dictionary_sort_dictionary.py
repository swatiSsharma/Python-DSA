
my_details = {
               "Swati" : { "age": 67, "gender": "Female"},
               "Clara" : { "age": 52, "gender": "Female"},
               "Eric" : { "age": 58, "gender": "Male"},
               "John" : { "age": 66, "gender": "Male"},
             }

print(my_details.items())
print()
x = sorted(my_details.items(), key = lambda x: x[1]["age"])
print(x) ## list with tuple inside
print()


my_details = {
               "Swati" : { "age": 67, "gender": "Female"},
               "Clara" : { "age": 52, "gender": "Female"},
               "Eric" : { "age": 58, "gender": "Male"},
               "John" : { "age": 66, "gender": "Male"},
             }

print(my_details.items())
print()
x = sorted(my_details.items(), key = lambda x: x[1]["age"])
print(x) ## list with tuple inside
print()

print(dict(x))