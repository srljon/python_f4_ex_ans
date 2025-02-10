"""
Write a program to count how many times "2" element appears in a
given list using a while loop.
digits = "1263451234123426346435"

1. Use a while loop to iterate through the numbers.
The variable "i" increases from O to len(digits) )
2. Increase count variable if digit is equal to "2"
3 Print the accumulated result
Expected output: 4
"""

# Define the string of digits
digits = "1263451234123426346435"

# Initialize index and count variables
i = 0
count = 0

# Use a while loop to iterate through the string
while i < len(digits):
    if digits[i] == "2":  # Check if the digit is "2"
        count += 1  # Increase count if condition is met
    i += 1  # Increment the index

# Print the accumulated result
print(count)

