"""
Create a formula to calculate the compound interest using
Python operators. Compound interest is calculated on the initial
principal and also on the accumulated interest of previous
periods.

Formula: A = P(1 + r/n)^(nt)

A: Amount
P: Principal
r: Rate
n: Number of times interest applied per time period
t: Number of time periods elapsed

Create a formula to calculate the compound interest using
Python operators. Compound interest is calculated on the initial
principal and also on the accumulated interest of previous
periods.

** Implement and calculate the following equation in Python:

A = 1000 *（ 1 + 0.05/12)**(12*5)

Answer: Approximately 1283.36

"""

# Initial principal
P = 1000
# Rate of interest
r = 0.05
# Number of times interest applied per time period
n = 12
# Number of time periods elapsed
t = 5
# Calculate the compound interest
A = P * (1 + r/n)**(n*t)
# Print the result
print(A)

