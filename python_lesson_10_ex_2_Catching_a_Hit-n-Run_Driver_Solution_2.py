# Clue 3: The 4-digit license plate number is a perfect square.
# We need to find a 4-digit number, so its square root will be between:
# sqrt(1000) approx 31.6 -> smallest integer base is 32 (32*32 = 1024)
# sqrt(9999) approx 99.99 -> largest integer base is 99 (99*99 = 9801)

# Initialize the base number for squaring
i = 32
found_license_plate = -1 # Use -1 or None to indicate not found yet

# Main while loop to iterate through possible base numbers
while i <= 99:
    perfect_square = i * i # This is our candidate license plate number (satisfies Clue 3)

    # Convert the number to a string to check its digits
    s_num = str(perfect_square)

    # Extract digits
    # s_num[0] is the first digit, s_num[1] is the second, and so on.
    digit1_char = s_num[0]
    digit2_char = s_num[1]
    digit3_char = s_num[2]
    digit4_char = s_num[3]

    # Clue 1: "The first two digits of the license plate number are the same."
    clue1_met = (digit1_char == digit2_char)

    # Clue 2: "The last two digits of the license plate number are the same,
    #          but different from the first two digits."
    # This means (digit3 == digit4) AND (digit1 != digit3)
    # We use digit1_char as the representative for the first pair of digits,
    # and digit3_char as the representative for the second pair.
    clue2_met = (digit3_char == digit4_char) and (digit1_char != digit3_char)

    # Check if all clues are met
    if clue1_met and clue2_met:
        found_license_plate = perfect_square
        # print(f"Found the license plate number: {found_license_plate}") # Optional: print immediately
        break # Exit the loop as we've found the unique answer

    i += 1 # Increment to check the next base number

# After the loop, print the result
if found_license_plate != -1:
    print(f"The license plate number is: {found_license_plate}")
else:
    print("No license plate number found matching all clues.")

