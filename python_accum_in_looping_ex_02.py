"""
Write a Python program using a while loop to calculate the total
number of apples Alice will have eaten after 30 days, assuming she
starts with one apple on the first day and doubles the number each
subsequent day. (i.e., 1 + 2 + 4+... + ?).

1. Use a while loop to iterate through the 30 days.
2. Accumulate the total number of apples eaten over the 30 days.
3. Print the final total of apples eaten.
"""

# Initialize variables
i = 1                  # Day counter
total = 0             # Running total of apples eaten

# Calculate total apples eaten over 30 days
while i <= 30:
    total = total + 2**(i-1)    # Add apples eaten on current day: 2^(day-1)
                                # Day 1: 2^0 = 1 apple
                                # Day 2: 2^1 = 2 apples
                                # Day 3: 2^2 = 4 apples, and so on...
    i = i + 1                   # Move to next day

# Display the total number of apples eaten
print(total)                    # Print final sum of all apples eaten