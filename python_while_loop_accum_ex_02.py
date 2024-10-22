"""
Write a Python program using a while loop to calculate the product of
all integers from 10 down to 1.

1. Use a while loop to iterate through the numbers from 10 to 1.
2. Accumulate the product of all these numbers.
3. Print the final product.

The final product number is 3628800
Save your file as "ClassNumber_YourName_Ex02_py"
"""

i = 10
product = 1

while i >= 1:
    product = product * i
    i = i - 1

print(product)
