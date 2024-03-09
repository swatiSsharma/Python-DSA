print('\nVariation 1\n')

def replace_character(org_str, target_char, replaced_with) -> str:
    modified_str = ''
    for char in org_str:
        if char == target_char:
            modified_str += replaced_with
        else:
            modified_str += char
    return modified_str

# Example usage:
input_string = 'delhi is a clean city'
target_char = 'i'
replaced_with = 'z'

result = replace_character(input_string, target_char, replaced_with)
print("Original String:", input_string)
print("String after replacement:", result)

# Variation 2
print('\nVariation 2\n')
a = 'delhi is a clean city'
r = a.replace('i', 'z')

print(a, '\n', r)

# Variation 3
print('\nVariation 3\n')
def replaceChar(string: str) -> str:
    ##new_string = ''  # or new = ""
    new_string: str = str()

    for char in string:
        if char.lower() == 'i':
            new_string += 'z'

        else:
            new_string += char

    return  new_string

print(replaceChar("This is an example sentence."))

# Variation 4
print('\nVariation 4\n')
a = 'delhi is a clean city'
lst = list(a)
result = "".join([ch if ch.lower() != 'i' else 'z' for ch in lst])

print(result)