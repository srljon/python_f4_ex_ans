"""
The Second Largest Digit of the Entered Number
Create a Python script to find the second largest digit of a number entered by a user.
1. Prompt the user to enter a number.
2. Iterate through each digit of the number.
3. Find the second largest digit of the entered number.
4. Print the second largest number.
"""

# Get input from user and store as string (strings are easier to iterate through)
number = input("Please enter a non-negative number: ")

# Initialize tracking variables with -1 (since all digits will be 0-9)
# We use -1 as a sentinel value that's smaller than any possible digit
largest_digit = -1
second_largest_digit = -1

# Initialize index to track position in string
index = 0

# Process each digit in the number using while loop
while index < len(number):
    # Get current digit and convert to integer
    current_digit = int(number[index])
    
    # Case 1: If we found a new largest digit
    if current_digit > largest_digit:
        # The old largest digit gets demoted to second largest
        # Then the current digit becomes the new largest
        second_largest_digit = largest_digit
        largest_digit = current_digit
    
    # Case 2: If the digit is between largest and second largest
    elif current_digit < largest_digit and current_digit > second_largest_digit:
        # Update second largest but keep the largest unchanged
        second_largest_digit = current_digit
    
    # Move to next digit
    index += 1

# If second_largest is still -1, it means we never found a second unique digit
# This happens when all digits in the number are the same (e.g., "333")
if second_largest_digit == -1:
    print(f"There is no second largest digit in {number} as all digits are the same.")
else:
    print(f"The second largest digit in the number {number} is {second_largest_digit}.")
