name = "Swati"
age = 16
gender = "Female"

# Method 1 - using Commas

print('My name is ',name)
print('My age is ', age)
print('My gender is ', gender)
print('My name is ',name,'My age is ', age,'My gender is ', gender)


# Method 2 - using F string
print(f'My name is {name}')
print(f'My age is {age}')
print(f'My gender is {gender}')
print(f'My name is {name}, My age is {age} and My gender is {gender}')

## Debugging
print(f"name = {name}")
print(f"{name }") # this would help in debugging -- gives variable value with datatype
print(f'{age = }')
print(f'{name,age,gender = }') # the result will be in tuple format with datatype and value of the variables

# Method 3

