"""
Implement a function that uses Python's input() to check if the
user's input is an empty string:

value = input( 'Please enter some text here: ' )

1. if the input value is empty, the function should print "Input value is empty.".

2. if the input value is not empty, the function should print "Input value is not empty.".
"""

# Prompt user for input and store the response
value = input( 'Please enter some text here: ' )

# Check if the input string is empty
if value == '':         # Compare input against an empty string ''
    print('Input value is empty.')      # Message if user just pressed Enter without typing
else:
    print('Input value is not empty.')  # Message if user typed any characters
