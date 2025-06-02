numbers = [12, -7, 34, -19, 8, -3, 25, -42, 16, -11, 7, -28, 45, -9, 5, -14, 20, -6, 33, -21]
final_list = []
i = 0

while i < len(numbers):
    if numbers[i] > 0 and len(final_list) < 5:
        final_list.append(numbers[i])
    i += 1

print(final_list)