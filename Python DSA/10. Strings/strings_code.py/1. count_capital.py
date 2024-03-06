# Count Capital letters in a given string 
a = "Python is A Great LAnGUAgE"

cnt = 0
for char in a:
    if 65 <= ord(char) <= 90:
        cnt += 1

print(cnt)

cnt = 0
for char in a:
    if 'A' <= char <= 'Z':
        cnt += 1

print(cnt)
# in comparision operator the values are automatically converted to ascii, only valid for strings