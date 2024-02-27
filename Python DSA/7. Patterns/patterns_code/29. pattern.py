# Pattern 29
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
n: int = int(input("Enter the number of rows:"))
for i in range(1, n+1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()
for i in range(n-1, 0, -1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print("*", end=" ")
    print()