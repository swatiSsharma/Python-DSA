"""
 Continously ask a string unless q/Q is entered
 and print previous strings
"""
# Variation 1
print('\nVariation 1\n')
result = 'a'  # initial value of result
while True:

    user_input = input('Enter the string: ')

    if user_input.lower() == 'q':  # Checking for both lowercase and uppercase "q".
        break
    else:
        result +=  user_input + ' '   # Append to previously stored results
    
print(result)

# Variation 2
print('\nVariation 2\n')
previous_strings = []

while True:
    user_input = input("Enter a string (type 'q' or 'Q' to quit): ")

    if user_input.lower() == 'q':
        break

    previous_strings.append(user_input)

print("\nPreviously entered strings:")
for i, string in enumerate(previous_strings, 1):
    print(f"{i}. {string}")
