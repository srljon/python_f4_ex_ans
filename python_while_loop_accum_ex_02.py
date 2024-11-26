"""
Write a Python program using a while loop to calculate the product of
all integers from 10 down to 1.

1. Use a while loop to iterate through the numbers from 10 to 1.
2. Accumulate the product of all these numbers.
3. Print the final product.

The final product number is 3628800
Save your file as "ClassNumber_YourName_Ex02_py"
"""

# Initialize the starting number (10)
i = 10
# Initialize the product accumulator to 1 (multiplying by 1 doesn't change a number)
product = 1

# Continue loop as long as i is greater than or equal to 1
while i >= 1:
    # Multiply the current number (i) with the accumulated product
    product = product * i
    # Decrease i by 1 for the next iteration
    i = i - 1

# Print the final result (10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
print(product)
