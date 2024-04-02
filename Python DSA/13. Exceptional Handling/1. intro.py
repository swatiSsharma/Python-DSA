# Exceptional Handling

'''
Exception handling is a programming paradigm aimed at handling errors and unexpected situations that 
may occur during the execution of a program. These errors could be due to various reasons such as 
invalid inputs, hardware failures, network issues, or programming mistakes.

In most programming languages, including Python, Java, C#, and others, exception handling typically 
involves the following components:

Try block: This block contains the code that might raise an exception. It is the portion of code where 
you anticipate potential errors.

Except block: This block is used to handle exceptions that occur within the try block. If an exception 
occurs, the control flow jumps to the corresponding except block. You can have multiple except blocks 
to handle different types of exceptions.

Finally block (optional): This block is used to execute cleanup code, regardless of whether an 
exception occurred or not. It is executed whether an exception occurred or not.

Here's a simple example in Python:
'''
try:
    # code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("No exception occurred.")
finally:
    print("Execution completed.")

'''
In this example:

The try block contains code that may raise exceptions, such as attempting to divide by zero or entering a non-integer value.
The except blocks catch specific types of exceptions (ValueError and ZeroDivisionError) and handle them accordingly.
The else block is executed if no exception occurs within the try block.
The finally block is executed regardless of whether an exception occurred or not, and it's typically used for cleanup operations.
Exception handling helps in writing more robust and reliable code by gracefully handling errors and preventing program crashes. It also facilitates better debugging by providing insights into what went wrong during program execution.
'''

