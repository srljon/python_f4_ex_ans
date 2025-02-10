"""
Write a Python program to find the largest number in a list using a
while loop.
numbers = [3, 1, 4, 1, 5, 9, 1, 2, 7, 3, 10, 13, 4, 6, 7, 1, 2, 6, 9, 5, 31

1. Use a while loop to iterate through the numbers.
( The variable "j" increases from O to len (numbers) )
2. Update the maximum number if the current number is greater than
the stored value.
3. Print the accumulated result
Expected output: 13

"""

# Define the list of numbers
numbers = [3, 1, 4, 1, 5, 9, 1, 2, 7, 3, 10, 13, 4, 6, 7, 1, 2, 6, 9, 5, 3]

# Initialize index variable to start from the first element
i = 0

# Initialize the variable 'largest' to store the maximum value found in the list
# It is initially set to 0 (assuming all numbers in the list are positive)
largest_num = 0 # Better way to use, avoiding negative numbers: largest_num = numbers[0]

# Use a while loop to iterate through all elements in the list
while i < len(numbers):
    # Check if the current number is greater than the stored 'largest' value
    if numbers[i] > largest_num:
        # Update 'largest' with the current number if it is greater
        largest_num = numbers[i]
    # Increment the index to move to the next element in the list
    i += 1

# Print the largest number found in the list
print(largest_num)