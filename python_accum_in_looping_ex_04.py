"""
If Mr Peter plans to purchase an Apple Vision Pro priced at $3499, he
intends to save money by setting aside $1 per day. Moreover, he aims to
increase his daily savings by $2, that means saving two dollars more
than the previous day. How many days will it take for Peter to
accumulate enough money to buy the Apple Vision Pro?

1. Use a while loop to loop untill the saved money greater than $3499.
2. Calculate the saving money for each day.
3. Calculate the total amount saved for each day.
4. Print the final total amount accumulated.
"""

# Initialize variables
day_s = 1
base_saving = 1  # Peter starts saving $1 on the first day
total = 0

# Loop until the total savings exceed $3499
while total <= 3499:
    daily_saving = base_saving + 2 * (day_s - 1)  # Calculate daily savings
    total += daily_saving  # Add daily savings to total
    print(day_s, daily_saving, total)  # Print the day, daily savings, and total savings
    day_s += 1  # Move to the next day

