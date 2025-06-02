i = 1
while i < 10:
    j = 1
    while j < 10:
        product = i * j
        # Print each product followed by a tab space
        print(product, end="\t")
        j += 1
    # Move to a new line after finishing one row
    print()
    i += 1