# Traversing in Dictionary

'''
Traversing, or iterating, through a dictionary in Python involves going through its keys, values, or 
key-value pairs. Here are different ways to traverse a dictionary:
'''
## 1. Iterating Over Keys:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

#  Using a for loop to iterate over keys
for key in my_dict:
    print(key)

## 2. Iterating Over Values:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

# Using a for loop to iterate over values
for value in my_dict.values():
    print(value)

## 3. Iterating Over Key-Value Pairs:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

# Using a for loop to iterate over key-value pairs
for key, value in my_dict.items():
    print(key, "->", value)

## 4. Checking for Existence and Iterating:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

# Checking for existence and iterating over key-value pairs
for key in my_dict:
    if key == "banana":
        print("Found 'banana' with value:", my_dict[key])

## 5. Using enumerate for Index and Value:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

# Using enumerate to get both index and value
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Item {index + 1}: {key} -> {value}")

## 6. Iterating Over Sorted Keys:
my_dict = {"apple": 2, "banana": 3, "orange": 5}

# Iterating over keys in sorted order
for key in sorted(my_dict):
    print(key, "->", my_dict[key])

'''
These examples demonstrate various ways to traverse a dictionary in Python, depending on your 
specific requirements. Choose the method that best fits the task at hand, whether you need to work 
with keys, values, or both.
'''