"""
Summing the Digits of a Number
Write a Python program that asks the user to input a number and then calculates the
sum of its digits.
1. Prompt the user to enter a number.
2. Extract each digit from the number entered by the user.
3. Sum all the digits of the number.
4. Print the result of the sum.
"""

# Prompt the user to input a non-negative number
# The input() function returns the number as a string, which makes it easier to process digit by digit
number = input("Please enter a non-negative number: ")

# Initialize variables:
# digit_sum: keeps track of the running total of all digits
# i: counter variable for traversing through each character of the number string
digit_sum = 0
i = 0

# Loop through each character in the number string
# Convert each character to an integer using int() and add it to digit_sum
while i < len(number):
    digit_sum += int(number[i])
    i += 1

# Display the final sum of all digits in the original number
# f-strings (formatted string literals) allow us to embed expressions inside string literals using {}
print(f"The sum of digits in {number} is: {digit_sum}")
