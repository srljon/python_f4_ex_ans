"""
Mr. Jon wants to buy a high-end Play Station 5 gaming console priced at
$2,499. He saves money by setting aside $10 on the first day.
Additionally, He plans to increase his daily savings by $5 each
subsequent day, meaning he saves five dollars more than the previous
day. How many days will it take for jon to accumulate enough money to
buy the gaming console?

1. Use a while loop to loop untill the saved money greater than $2499.
2. Calculate the saving money for each day.
3. Calculate the total amount saved for each day.
4. Print the final total amount accumulated.
"""

# Initialize variables
day = 1
base_saving = 10  # Jon starts saving $10 on the first day
total = 0

# Loop until the total savings exceed $2,499
while total <= 2499:
    daily_saving = base_saving + 5 * (day - 1)  # Calculate daily savings
    total += daily_saving  # Add daily savings to total
    print(f"Day {day}: Saved ${daily_saving}, Total: ${total}")  # Print daily progress
    day += 1  # Move to the next day

# Print final results
# f-strings (formatted string literals) allow us to embed expressions inside string literals using {}
print(f"\nIt took {day-1} days to save ${total}")

