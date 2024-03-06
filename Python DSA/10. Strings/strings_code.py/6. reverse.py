# reverse the string, reverse the words

my_string = input("Enter the string: ") ##" python is a great language"

result = my_string.split()
result = result[::-1]

s = " ".join( i for i in result)
print(s)