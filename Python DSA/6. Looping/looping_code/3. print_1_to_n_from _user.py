# Write a function that prints numbers from 1 to n. The function should take an integer n
# (Print 1 to N)

# Variation 1
i: int = 1
while i <= 10:
    print(i)
    i += 1

# Variation 2
i: int = 1
while i <= 10:
    print(i, end = " ")
    i += 1

# terminal ctrl + C --> incase of infinite loop