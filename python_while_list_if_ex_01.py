"""
Print All Odd Numbers in a List
digits = |1, 2, 6, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 4, 2,
1. Use a while loop to iterate through the numbers.
( The variable "j" increases from O to len(digits) )
2. Print the digit if digit is equal to Odd number
3. Print the result
Expected output:
1
3 
1
"""

# Define the list of digits
digits = [1, 2, 6, 3, 4, 5, 1, 2, 3, 4, 1, 2, 3, 4, 2, 6, 3, 4, 6, 4, 3, 5]

# Initialize the index variable
i = 0

# Use a while loop to iterate through the list
while i < len(digits):
    if digits[i] % 2 != 0:  # Check if the number is odd
        print(digits[i])  # Print the odd number
    i += 1  # Increment the index
