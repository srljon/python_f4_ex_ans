"""
Write a Python program using a while loop to calculate the sum of all
numbers from 1 to 100 (i.e., 1 + 2 + 3+ ... + 100).

1. Use a while loop to iterate through the numbers.
2. Accumulate the sum of all numbers between 1 and 100, inclusive.
3. Print the final sum. The final sum number is 5050.
"""

# Initialize variables
i = 1                  # Counter starting from 1
total = 0             # Running sum, starts at zero

# Calculate sum of numbers from 1 to 100
while i <= 100:
    total = total + i    # Add current number to running total
                        # First iteration: total = 0 + 1
                        # Second iteration: total = 1 + 2
                        # Third iteration: total = 3 + 3, and so on...
    i = i + 1           # Move to next number

# Display the final sum
print(total)            # Print sum of all numbers from 1 to 100 (should be 5050)