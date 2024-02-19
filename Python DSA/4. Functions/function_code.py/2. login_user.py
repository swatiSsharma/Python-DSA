# Login user

def loginUser(username, password):
    # Define a set of valid credentials (you might want to replace this with a database check in a real application)
    valid_credentials = {'user1': 'password123', 'user2': 'secret123'}

    # Check if the provided username exists and the password matches
    if username in valid_credentials and valid_credentials[username] == password:
        return True  # Login successful
    else:
        return False  # Login failed

# Example usage:
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

if loginUser(username_input, password_input):
    print("Login successful!")
else:
    print("Login failed. Please check your username and password.")

