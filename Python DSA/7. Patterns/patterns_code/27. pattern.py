# Pattern 27
# enter the number of lines by the user
'''
N = 9
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

N = 10
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''

def patternLinesInput(lines: int) -> None:
    rows: int = lines / 2 
    
    if  rows % 2 == 0.5:
        n = lines // 2 + 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=' ')
            print()
        
        for i in range(n, 0, -1):
            for j in range(1, i):
                print(j, end = ' ')
            print()
    else:
        n = lines // 2
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=' ')
            print()
    
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end = ' ')
            print()

lines: int = int(input("Enter the number of rows:"))
patternLinesInput(lines)
print('\n NUMBER OF LINES AS 9\n')
patternLinesInput(9)
print('\n NUMBER OF LINES AS 10\n')
patternLinesInput(10)