# Ask a string from user replace all vowels with z

 
## VARITATION 1
user_input = input("Enter a string: ")

modified_string = list(user_input)

string = ''.join(['z' if char.lower() in 'aeiou' else char for char in modified_string])

print(string)


## VARITATION 2
s = user_input
vowels = ['a', 'e', 'i', 'o', 'u']

l = list(s)

for i in range(len(l)):
    if l[i] = 'z'
print(l)

output = "".join(str(i) for i in l)
print(output)

## VARIATION 3
string: str = user_input  # python
vowels = ["a", "e", "i", "o", "u"]
new_string = "".join([i if i.lower() not in vowels else "z" for i in string])
print(new_string)


## VARIATION 4

str = user_input
str2 = ""

for ch in str:
    if ch.lower() in 'aeiou':
        str2 += 'z'
    else:
        str2 += ch

print(str2)