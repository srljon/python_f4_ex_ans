limit = 30

a = 1
while a <= limit:
    # Initialize b starting from a in each iteration of the outer loop
    # This ensures that b >= a, preventing duplicates like (4, 3, 5) after (3, 4, 5)
    b = a
    while b <= limit:
        # Initialize c starting from b in each iteration of the middle loop
        # Since a^2 + b^2 = c^2, c must be >= b (and >= a).
        # This helps reduce checks and ensures the triplet order if desired.
        c = b
        while c <= limit:
            # Check the Pythagorean condition
            if a**2 + b**2 == c**2:
                # Found a valid triplet (a, b, c) where a <= b <= c
                # Print in the required format
                print(f"{a}, {b}, {c}")
                # Optional optimization: Once a matching c is found for a given a and b,
                # no larger c will satisfy a^2 + b^2 = c^2. We could 'break' the
                # innermost loop here, but it's not strictly necessary for correctness.
                # break

            # Increment the innermost loop counter
            c += 1

        # Increment the middle loop counter
        b += 1

    # Increment the outermost loop counter
    a += 1
