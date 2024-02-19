# Pass

"""
In Python, the pass statement is a no-operation statement. It is used when a statement is syntactically
required but you want to do nothing. It is often used as a placeholder in situations where the syntax 
requires a statement, but no action is desired or necessary.

When it comes to functions, you might use pass as a placeholder when defining a function that you plan to implement later. For example:
"""

def placeholder_function():
    pass

"""
In this case, the placeholder_function is defined, but it doesn't do anything yet. You can later add the actual implementation without changing the function signature.

Here's an example of a more practical use case:
"""

#def process_data(data):
#    # some code to process data
#    pass

# Later in the code, you can implement the function
def process_data(data):
    # actual implementation
    print(f"Processing data: {data}")

"""
This way, you can define the function early in your code structure and fill in the implementation 
details when you are ready.

It's important to note that using pass as a placeholder should be done with caution. If you use it 
excessively, it might indicate incomplete or missing functionality in your code, so it's a good 
practice to comment on why pass is being used if it's not immediately obvious.
"""

# if there are function with same name the 1st function takes priority as in python 
# functions are executed top to down
