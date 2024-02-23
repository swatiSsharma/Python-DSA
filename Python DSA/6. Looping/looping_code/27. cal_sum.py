# Enter a number by user continously unless 0 is entered. Calculate the sum of previous numbers


total = 0

while True:
    user_input = int(input("Enter a number (enter 0 to exit): "))
    
    if user_input == 0:
        break 
    
    total += user_input
    
print("Total so far:", total)