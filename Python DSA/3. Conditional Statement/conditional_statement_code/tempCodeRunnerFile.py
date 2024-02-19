student = input('Are you a student').lower()
if student == 'yes':
    class_attented = int("Enter class attendted")
    if class_attented >= 20:
        assignment  = int("Enter assignment submitted")
        if assignment >= 45:
            print("you are eligible for certificate")
    else:
            print('you are not eligible') 
else:
            print('you are not eligible')