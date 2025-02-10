"""
Check if a List is Sorted in Ascending Order
Write a Python program to check if a given list is sorted in ascending
order or not. If the list is sorted, print "The list is sorted", otherwise
print "The list is not sorted".
numbers = [1, 4, 6, 9, 13, 14, 17, 21, 26, 31, 34, 39, 43,
1. Use a while loop to iterate through the numbers.
( The variable "j" increases from O to len(numbers) )
2. Check if the current number is greater than the previous one.
3. Print "The list is sorted", if sorted, otherwise print "The list is not
sorted".

"""

# Define the list of numbers
numbers = [1, 4, 6, 9, 13, 14, 17, 21, 26, 31, 34, 39, 43, 47, 50, 54, 59, 63, 
           67, 72, 76, 81, 85, 90, 93, 97, 100]

# Initialize index variable to start checking from the first element
i = 0

# Initialize a boolean flag 'is_sorted' to assume the list is sorted
is_sorted = True

# Use a while loop to iterate through the list and check if it's sorted
while i < len(numbers) - 1:  # Iterate up to the second-last element
    if numbers[i + 1] < numbers[i]:  # If a later element is smaller than the current one
        is_sorted = False  # The list is not sorted
        break  # Exit the loop early since we found an unsorted pair
    i += 1  # Move to the next element

# Check the result and print whether the list is sorted or not
if is_sorted:
    print("The list is sorted")
else:
    print("The list is not sorted")


