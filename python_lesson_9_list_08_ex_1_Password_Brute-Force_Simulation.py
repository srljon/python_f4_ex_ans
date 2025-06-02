import hashlib

# The target hash we are looking for
known_hash = "7a698699a9229b278afa72593214582d739b9bad"
matched_found = False

# Loop for the first digit (hundreds place)
d1 = 0
while d1 < 10 and not matched_found:
    # Loop for the second digit (tens place)
    d2 = 0
    while d2 < 10 and not matched_found:
        # Loop for the third digit (units place)
        d3 = 0
        while d3 < 10 and not matched_found:
            # 1. Construct the 3-digit password string for the current combination
            #    Example: d1=0, d2=0, d3=1 -> "001"
            #             d1=1, d2=2, d3=3 -> "123"
            password_str = str(d1) + str(d2) + str(d3)

            # 2. Convert to bytes and compute SHA-1 hash
            sha1_hash = hashlib.sha1(password_str.encode('utf-8')).hexdigest()

            # 3. Compare with the known hash
            if sha1_hash == known_hash:
                # 4. If matched, print the password and set flag to stop loops
                print(password_str)  # Requirement 5: Print only the matched password
                matched_found = True
                # No need for 'break' here, 'matched_found' will stop this loop
                # and prevent outer loops from continuing their iterations.

            # Increment the innermost loop counter
            d3 += 1
        # Increment the middle loop counter
        d2 += 1
    # Increment the outermost loop counter
    d1 += 1