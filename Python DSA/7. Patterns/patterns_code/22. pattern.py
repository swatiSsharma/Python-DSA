# Pattern 22
'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows):
            print(" ", end=" ")
        for  k in range(i):
            print("*", end=" ")
        print()
        
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)
