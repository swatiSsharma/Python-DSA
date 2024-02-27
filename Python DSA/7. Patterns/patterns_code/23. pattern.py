# Pattern 23
'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows):
            print(" ", end=" ")
        for  k in range(1, i+1):
            print(k, end=" ")
        print()
        
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)