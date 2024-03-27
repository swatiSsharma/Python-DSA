# Get message of error and error type

try:
    my_list = [34, 55, 63, 78, 94, 0]
    print(my_list)
    print(my_list[99])  # Trying to access an index that doesn't exist
    # print(my_list[0] / my_list[-1])
except ZeroDivisionError:
    print("Cannot divide by zero, please check the values again")
except IndexError as e:
    print("Error:", e.__class__.__name__, ' : ', e)  # Getting the name of the exception
   # these gives the type of error
    # print(type(e).__name__, e.__class__.__name__)
    print("Index is out of range")
except Exception as e:
    print("Error:", e.__class__.__name__)  # Getting the name of the exception
    print(e)
    print("Some unknown error occurred")
else:
    print("Everything works fine")
finally:
    print("This is a finally clause")
