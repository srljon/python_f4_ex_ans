# Given variables
rows = 10
seats_per_row = 15

# Initialize current row counter
current_row = 0

# Outer while loop to iterate over all the rows
while current_row < rows:
    # Initialize current seat counter for each row
    current_seat = 0
    # Inner while loop to iterate over seat numbers
    while current_seat < seats_per_row:
        # Determine if the seat should be a person 'P' or a gap '_'
        # The output example suggests that the 3rd, 6th, 9th, etc. seats are gaps.
        # In 0-indexed terms, these are seats 2, 5, 8, ...
        # So, if (current_seat + 1) is a multiple of 3, it's a gap.
        if (current_seat + 1) % 3 == 0:
            print("_", end=" ")  # Print '_' for a gap, followed by a space
        else:
            print("P", end=" ")  # Print 'P' for a person, followed by a space

        current_seat += 1  # Move to the next seat

    print()  # Move to the next line after printing all seats in a row
    current_row += 1  # Move to the next row
