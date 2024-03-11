'''

'''
my_dict ={
    'name':'John',
    'akul': 11,
    'muskan': 56,
    'sanjay': None # not a best way for declared with a value None
}
keyname = 'sanjay' #input("Enter the key name: ")
print('Method 1')
x = my_dict.get(keyname)
if x is None:
    print("Key not found")
else:   
    print(x)

## Better way or only way
print('\nMethod 2')
if keyname in my_dict:
    print(my_dict[keyname])
else:
    print("Key not found")