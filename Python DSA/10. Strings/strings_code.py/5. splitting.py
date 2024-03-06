my_string = " pythonn= is a great language"

result = my_string.split()

# splits by whitespaces -> spaces, tab and  newlines
print(f'Result: {result}')

result = my_string.split('n=')
print(result)

## the split delimiter will not be included