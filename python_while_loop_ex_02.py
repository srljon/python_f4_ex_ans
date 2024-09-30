"""
Write a Python program that allows the user to input a number to be
used as an increment or decrement in two while loops. The first loop
should start at 1 and continue until it reaches or exceeds 100. The
second loop should start at 100 and continue until it reaches or goes
below 1. The program should print each value in both loops.

steps = int( input( 'Enter a positive increment/decrement value: ' ) )

1. Prompt the user to input a positive integer for incrementing from 1 to 100.
2. Use the same value for decrementing from 100 to 1.
3. Ensure the input is a positive integer. If not, display an error message and prompt again.
4. Use while loops to iterate and print values.
"""

steps = int( input( 'Enter a positive increment/decrement value: ' ) )

while steps <= 0:
    print("Error: Please enter a positive value!!")
    steps = int( input( 'Enter a positive increment/decrement value: ' ) )

number_increment = 1

while number_increment <= 100:
    print(number_increment)
    number_increment += steps

number_decrement = 100

while number_decrement >= 1:
    print(number_decrement)
    number_decrement -= steps
