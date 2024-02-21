# Ask a number from user ie 50 then print -50 to 50 and -50 then print from 50 to -50

user_number = int(input("Enter a number: "))

if user_number >  0:   # 50 --> -50 to 50
    start = -user_number  
    end = user_number 
    # print(start, end, "positive value")
    while start <= end:
        print(start, end= " ")
        start += 1

else: # -50 --> 50 to -50
    start = abs(user_number) # The result is always a non-negative number 
    end = user_number 
    # print(start, end, "negative value")

    while start >= end:
        print(start, end= " ")
        start -= 1