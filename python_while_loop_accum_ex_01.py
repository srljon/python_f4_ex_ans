"""
Write a Python program using a while loop to calculate the sum of all
odd numbers from 1 to 99 (i.e., 1, 3, 5, ..., 99).

1. Use a while loop to iterate through the numbers.
2. Accumulate the sum of all odd numbers between 1 and 99, inclusive.
3. Print the final sum.
The final sum number is 2500
Save your file as "ClassNumber_YourName_Ex01.py"
"""

i = 1
total = 0

while i <= 50:
    total = total + (2*i - 1)
    i = i + 1

print(total)
