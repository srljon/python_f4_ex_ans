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

# Initial principal amount (starting investment)
P = 1000  # $1000 as the initial deposit

# Annual interest rate (5% expressed as 0.05)
r = 0.05  # 5% annual interest rate

# Number of times interest is compounded per year
n = 12    # Monthly compounding (12 times per year)

# Total number of years for the investment
t = 5     # 5-year investment period

# Calculate the final amount using the compound interest formula
# A = P(1 + r/n)^(nt)
# Where (1 + r/n) is the interest factor per compounding period
# and (n*t) is the total number of times interest is compounded
A = P * (1 + r/n)**(n*t)

# Print the final amount after 5 years of compound interest
print(A)  # Result will be approximately 1283.36

