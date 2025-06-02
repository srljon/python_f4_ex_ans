prices = [150, 200, 50, 100, 75, 300, 125]
target = 250
i = 0

while i < len(prices):
    j = i + 1
    while j < len(prices):
        if (prices[i] + prices[j] == target):
            print(f"{prices[i]} + {prices[j]} = {target}")
            # Alternative 1: print(prices[i], " + ", prices[j], "=", target)
            # Alternative 2: print(f"{prices[i]:.2f} + {prices[j]:.2f} = {target:.2f}")
        j += 1
    i += 1
