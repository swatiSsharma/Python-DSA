# Pattern 21
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "* " * i
        print(spaces + stars)

# Adjust the number of rows as needed
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)
