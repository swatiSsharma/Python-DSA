# Pattern 28
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

def print_star_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i, rows):
            print(" ", end=" ")
        for  k in range(i):
            print("*", end=" ")

        for l in range(1, i):
            print("*", end=' ')
        print()
        
        
n: int = int(input("Enter the number of rows:"))
print_star_pattern(n)

for i in range(1, n + 1):
    for j in range(i, n):
        print(" ", end=" ")
    for  k in range(i*2-1): # inner star pattern incase of i=1 then 1 i=2 then 3 i=3 then 5 
        print("*", end=" ")
    print()