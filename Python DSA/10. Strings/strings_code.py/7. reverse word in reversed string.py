

my_string = "Python is great"  # nohtyp si taerg
lst = my_string.split()
lst = lst[::-1]
reversed_string = ' '.join( i[::-1] for i in lst)

print(reversed_string)