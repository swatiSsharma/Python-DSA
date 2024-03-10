'''
Ask a string from user. Replace all the space characters with “-”. Do not use replace() method.
'''
def replace_space(input_str: str):
    result_str = ""

    for char in input_str:
        if char == ' ':
            result_str += '-'
        else:
            result_str += char

    return result_str

print(replace_space("Hello World"))
print(replace_space('python is a great language'))