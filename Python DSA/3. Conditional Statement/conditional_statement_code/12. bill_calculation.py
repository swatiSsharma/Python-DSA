# Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

# Example 1
# Enter bill amount = 80000
# You got 30% discount
# Your final bill is Rs. 56000

# Get input from the user
final_amount = float(input("Enter the final amount of the bill: "))

# Initialize variables for discount and final bill
discount_percentage = 0
final_bill = final_amount

# Determine the discount based on the final amount
if final_amount >= 50000:
    discount_percentage = 30
elif 40000 <= final_amount <= 49999:
    discount_percentage = 25
elif 30000 <= final_amount <= 39999:
    discount_percentage = 20
elif 10000 <= final_amount <= 29999:
    discount_percentage = 10

# Calculate the discount and final bill
discount_amount = (discount_percentage / 100) * final_amount
final_bill -= discount_amount

# Print the discount and final bill
print(f"You got {discount_percentage}% discount")
print(f"Your final bill is Rs. {final_bill:.2f}")
