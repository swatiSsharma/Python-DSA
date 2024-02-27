# Pattern 25
'''
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows):
            print(" ", end=" ")
        for  k in range(i, 0, -1):
            print(k, end=" ")
        print()
        
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)