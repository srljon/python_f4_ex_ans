"""
Write a Python program using a while loop to calculate the total
amount Alice will have accumulated after 30 years, assuming she starts
with 10,000 dollars and reinvests the principal and interest at 5%
annually.

1. Use a while loop to iterate through the 30 years.
2. Accumulate the total amount of money accumulated over the 30 years.
3. Print the final total amount of money accumulated.
"""

# Initialize variables
i = 1                  # Counter for tracking years
total = 10000         # Initial investment amount in dollars

# Calculate compound interest over 30 years
while i <= 30:
    total = total * 1.05    # Increase amount by 5% interest rate (1.05 = 100% + 5%)
    i = i + 1              # Increment year counter

# Display results
print(total)               # Print raw total (includes many decimal places)
print(round(total, 2))     # Print total rounded to 2 decimal places (currency format)
