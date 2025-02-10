"""
Extracting Positive Numbers from a List
Write a Python program that takes a list of numbers (both positive and negative,
including zero) and extracts all the positive numbers (excluding zero) from the
list. Use a while loop and the append () method to achieve this.
numbers = [-5, 0, 12, -8, 3, 0, 7]

1. Use a while loop to iterate through the numbers.
( The variable "j" increases from O to len(numbers) )
2. Append only the positive numbers (greater than 0) to a new list.
3. Print the final list containing all the positive numbers.
Expect output: [12, 3, 7]
"""

# Define the list of numbers
numbers = [-5, 0, 12, -8, 3, 0, 7]

# Initialize an empty list to store positive numbers
positive_numbers = []

# Initialize index variable to start iterating from the beginning of the list
i = 0

# Use a while loop to iterate through all elements in the list
while i < len(numbers):
    # Check if the current number is positive
    if numbers[i] > 0:
        # If the number is positive, add it to the 'positive_numbers' list
        positive_numbers.append(numbers[i])
    
    # Move to the next index
    i += 1

# Print the final list of positive numbers
print(positive_numbers)
