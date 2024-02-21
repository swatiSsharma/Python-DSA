# Write a function to ask a number from user ie 50 then print -50 to 50 and -50 then print from 50 to -50
def print_number_ranges(user_number):
    if user_number > 0:
        start = -user_number
        end = user_number
        while start <= end:
            print(start, end=" ")
            start += 1
    else:
        start = abs(user_number)
        end = user_number
        while start >= end:
            print(start, end=" ")
            start -= 1

# Get user input for the number
user_number = int(input("Enter a number: "))
print_number_ranges(user_number)