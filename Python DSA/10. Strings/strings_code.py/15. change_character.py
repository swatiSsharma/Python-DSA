'''
Keep asking characters from user until he presses q on the keyboard.
Change all the capital letters to small, and all the small letters to capital.
(Don’t use swapcase() )
'''
char = input("Enter the character: ")
while True:
    if len(char) == 1:
        if char.lower() == 'q':
            break
        else:
            if 65 <= ord(char) <= 90:
                print(chr(ord(char) + 32)) # Convert to small case
            elif 97 <= ord(char) <= 122:    
                print(chr(ord(char) - 32)) # Convert to capital case
            else:
                print(char)                 # Print as it is if not a letter
            char = input("Enter the character: ")
    else:
        print("Please enter a single character.")