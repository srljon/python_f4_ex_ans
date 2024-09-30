"""
Implement a function that uses Python's input() to check if the
user's input is an empty string:

value = input( 'Please enter some text here: ' )

1. if the input value is empty, the function should print "Input value is empty.".

2. if the input value is not empty, the function should print "Input value is not empty.".
"""

value = input( 'Please enter some text here: ' )

if value == '':
  print('Input value is empty.')
else:
  print('Input value is not empty.')
