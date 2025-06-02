rows = 10
while rows > 0:
    seats_per_row = 15
    while seats_per_row > 0:
        seat_pairs = 3
        while seat_pairs > 0:
            if seat_pairs != 1:
                print( "P ", end="" )
            else:
                print( "_ ", end="" )
            seat_pairs -= 1
            seats_per_row -= 1

        if seats_per_row == 0:
            print()

    rows -= 1
