"""
Write a Python program using a while loop to calculate the sum of all
odd numbers from 1 to 99 (i.e., 1, 3, 5, ..., 99).

1. Use a while loop to iterate through the numbers.
2. Accumulate the sum of all odd numbers between 1 and 99, inclusive.
3. Print the final sum.
The final sum number is 2500
Save your file as "ClassNumber_YourName_Ex01.py"
"""

# Initialize counter variable
i = 1
# Initialize sum variable to store the running total
total = 0

# Loop runs 50 times because we need to generate 50 odd numbers (1 to 99)
while i <= 50:
    # Formula (2*i - 1) generates odd numbers:
    # When i=1: 2*1-1 = 1
    # When i=2: 2*2-1 = 3
    # When i=3: 2*3-1 = 5
    # And so on...
    total = total + (2*i - 1)
    # Increment counter
    i = i + 1

# Print the final sum of all odd numbers from 1 to 99
print(total)
