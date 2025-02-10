"""
Write a Python program that calculates the sum of digits.
digits = 78435683769834734829347239857298561024"
Use a while loop to iterate through the numbers.
( The variable "¡" increases from O to len(digits) )
(2 Print the accumulated result
Expected output: 
Sum of all digits: 199
"""

# Define the string of digits
digits = "78435683769834734829347239857298561024"

# Initialize the index and sum variables
i = 0
sum_of_digits = 0

# Use a while loop to iterate through the digits
while i < len(digits):
    sum_of_digits += int(digits[i])  # Convert each character to an integer and add to sum
    i += 1  # Increment the index

# Print the accumulated result
print("Sum of all digits:", sum_of_digits)
