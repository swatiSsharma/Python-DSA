# Certificate
'''
Take 3 user requirement but individually,

- Are you part of code and debug --> yes/no
- Minimum class attended should be 20
- minimum assignmnet submitted is 45
'''

part_of_code_debug: str= input('Are you a student of Code and Debug').lower()
if part_of_code_debug == "yes":
    class_attendance: int = int(input("Enter the number of classes attended: "))
    if class_attendance >= 20:
        assignment_submissions: int = int(input("Enter the number of assignment submissions: "))
        if assignment_submissions >= 45:
            print("You are eligible for Certificate")
        else:
            print("Not eligible for Certificate as minimum assignment submissions requirement is not met")  
    else:
        print("Not eligible for Certificate as minimum class attendance requirement is not met.")
else:
    print("Not eligible for Certificate as you are not part of  Code and Debug. Therefore, you are not eligible for the certificate.")

