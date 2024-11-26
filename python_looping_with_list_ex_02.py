"""
Count the Number of Twos in an Input Number
Create a Python script to count the occurrences of the digit "2" in a user-provided
integer. Display the count to the user.
1. Prompt the user to enter a number.
2. Iterate through each digit of the number.
3. Count how many times the digit "2" appears.
4. Print the counting number.
"""

# Get input from user and store it as a string
# Note: input() always returns a string, so no conversion is needed
number = input("Please enter a non-negative number: ")

# Initialize counter variable to keep track of how many 2's we find
count = 0

# Loop through each character in the number string
# We can treat strings like lists in Python, where each character is an element
while i < len(number):
    # Check if the current digit is '2'
    # Note: we use '2' (string) not 2 (integer) because number is a string
    if number[i] == '2':
        count += 1
    i += 1

# Print the result using an f-string
# f-strings (formatted string literals) let us embed variables inside {} in strings
print(f"The digit '2' appears {count} times in the number {number}.")
