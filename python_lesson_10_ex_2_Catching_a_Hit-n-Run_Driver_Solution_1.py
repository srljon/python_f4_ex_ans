import math
first_second_digit = 1
found_it = False

while first_second_digit < 10 and not found_it:
    third_fourth_digit = 0

    while third_fourth_digit < 10 and not found_it:

        if first_second_digit != third_fourth_digit:
            first_second_text = str(first_second_digit)*2
            third_fourth_text = str(third_fourth_digit)*2

            num_plate_digits = int(first_second_text + third_fourth_text)

            square_root_result = math.sqrt(num_plate_digits)

            if square_root_result == int(square_root_result):
                print(f"Found the license plate number: {num_plate_digits}")
                found_it = True

        third_fourth_digit += 1

    first_second_digit += 1

if not found_it:
    print("No license plate number found matching all criteria.")
