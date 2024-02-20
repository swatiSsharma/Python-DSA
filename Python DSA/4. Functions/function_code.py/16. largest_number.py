# Create a function that takes three numbers as parameters and returns the largest among them. Also 
# if no arguments are passed, make sure the parameters take default value as None and return answer 
# as -1

def largest(num1 = None, num2 = None, num3 = None) -> int:
    if num1 == num2 == num3 == None:
        return -1
    else:
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num3:
            return num2
        return  num3
    
print(largest(3, 4, 1))
print(largest())
