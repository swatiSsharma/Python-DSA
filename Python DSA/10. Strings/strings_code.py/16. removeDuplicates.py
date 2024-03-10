'''
Python Program to remove all duplicates from a given string
'''

def  remove_duplicates(string: str) -> str:
    withoutDup = ''
    for char in string:
        if char not in withoutDup:
            withoutDup += char
    
    return withoutDup


print(remove_duplicates("Hello World")) 
print(remove_duplicates("programming"))