# Pattern 24
'''
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows):
            print(" ", end=" ")
        for  k in range(1, i+1):
            print(i, end=" ")
        print()
        
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)