# Create a function named calSum() which takes 2 integers n1 and n2 as an argument. Calculate the 
# sum of all the numbers from n1 and n2 and RETURN THAT SUM. Also make sure that n1 is smaller than 
# n2. If it is not, then return “n1 should be smaller

def calSum(n1: int, n2: int):
    if n1 < n2:
        total = 0
        i: int = n1
        while i <= n2:
            total += i
            i += 1
        return total
    else:
        return 'n1 should be smaller'
    
n1: int = int(input("Enter the starting range: "))
n2: int = int(input("Enter the ending range: "))
print(calSum(n1, n2))
print(calSum(1, 10))
print(calSum(7, 3))