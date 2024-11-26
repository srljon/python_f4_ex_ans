"""
Implement a quadratic equation solver using
Python variables and operators. The quadratic formula is used
to find the roots of a quadratic equation in the form ax^2 + bx + c = 0.

** Implement and calculate the following equation in Python:

x = (-5 + (5^2 - (4x1x6)^0.5)) / 2x1 = -2.0

"""
# Write your code below this line 👇

# Breaking down the quadratic formula calculation:
# a = 1, b = 5, c = 6
# Formula: x = (-b ± √(b² - 4ac)) / (2a)

# Step by step:
# 1. Calculate b² (5²) = 25
# 2. Calculate 4ac (4 * 1 * 6) = 24
# 3. Calculate √(b² - 4ac) = √(25 - 24) = √1 = 1
# 4. Add -b and the square root (-5 + 1) = -4
# 5. Divide by 2a (2 * 1) = 2
x = (-5 + (5**2 - (4*1*6))**0.5) / 2*1

# Print the result (should be -2.0)
print(x)