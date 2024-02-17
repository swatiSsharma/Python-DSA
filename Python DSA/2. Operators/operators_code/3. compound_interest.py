# Write a Python program to calculate the compound interest for a given principal, rate of interest,
# and time period. Ask everything from the user.

principle: float = float(input('Enter the Principle Amount: '))
rate: float = float(input('Enter the Rate of Interest: '))
time: float = float(input('Enter the Length of time to invest: '))
    
ci = (principle * (1 + rate ) ** time) - principle

print('The compound interest for given input is Rupees {0} '.format(ci))
