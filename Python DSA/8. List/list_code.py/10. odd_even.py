# Odd Even using ternary within for loop

my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)] 
print(my_list)

my_list = [f"{i}~even" if i % 2 == 0 else f"{i}~odd" for i in range(1, 11)] 
print(my_list)