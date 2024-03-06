# Count Digits in given string

input_string = 'degy126563hjv924ujmf4i4932'
digit_count = 0
for char in input_string:
    if 48 <= ord(char) <= 57:
        digit_count += 1
print(digit_count)

digit_count = 0
for char in input_string:
    if '0'<= char <= '9':
        digit_count += 1
print(digit_count)

# in comparision operator the values are automatically converted to ascii only valid for strings        