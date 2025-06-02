numbers = [10, 15, 20, 5, 7, 9, 2, 3, 1, 4]
current_sublist = [numbers[0]]

i = 1

while i < len(numbers):
    if numbers[i] > numbers[i - 1]:
        current_sublist.append(numbers[i])
    else:
        print(current_sublist)
        current_sublist = [numbers[i]]
    i += 1

print(current_sublist)
