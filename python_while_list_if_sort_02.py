"""
Check if a List is a Palindrome
Write a Python program to check if a given list is a palindrome or not. A
palindrome list reads the same backward as forward. If the list is a palindrome,
print "The list is a palindrome", otherwise print "The list is not a palindrome".
numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]

1. Use two pointers to compare elements from the start and end of
the list, moving towards the center.
2. If any pair of elements differ, set a flag to indicate the list is not a
palindrome and exit the loop
3. Finally, print whether the list is a palindrome based on the flag's
value. 
"""

# Define the list of numbers
numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Initialize a boolean flag 'is_palindrome' to assume the list is a palindrome
is_palindrome = True

# Initialize index variable to start from the beginning of the list
i = 0

# Calculate the last index of the list
last_index = len(numbers) - 1

# Use a while loop to check if the list is a palindrome
while i < len(numbers) // 2:  # Only need to check up to the middle of the list
    # Compare the element from the front with the corresponding element from the back
    if numbers[i] != numbers[last_index - i]:
        is_palindrome = False  # If any mismatch is found, the list is not a palindrome
        break  # Exit the loop early

    i += 1  # Move to the next index

# Check the result and print whether the list is a palindrome or not
if is_palindrome:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")
