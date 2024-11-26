"""
The Largest Digit of the Entered Number
Create a Python script to find the maximum digit of a number entered by a user.
1. Prompt the user to enter a number.
2. Iterate through each digit of the number.
3. Find the largest digit of the entered number.
4. Print the largest number.
"""

# Store the user's input as a string - strings are easier to iterate through digit by digit
number = input("Please enter a non-negative number: ")

# Start by assuming the first digit is the largest
# We convert the first character to an integer using int()
largest_digit = int(number[0])

# Initialize an index to keep track of our position in the string
index = 0

# Iterate through each character using while loop
# Continue until we reach the end of the string (len(number))
while index < len(number):
    # Get the current digit using string indexing
    digit = number[index]
    
    # Compare and update largest digit if necessary
    if int(digit) > largest_digit:
        largest_digit = int(digit)
    
    # Move to next digit
    index += 1

# Display the result using an f-string for clean string formatting
# f-strings allow us to embed expressions inside string literals
print(f"The largest digit in the number {number} is {largest_digit}.")
