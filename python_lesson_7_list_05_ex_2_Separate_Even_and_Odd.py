numbers = [12, -7, 34, -19, 8, -3, 25, -42, 16, -11, 7, -28, 45, -9, 5, -14, 20, -6, 33, -21]

even_numbers = []
odd_numbers = []

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])
    i += 1

print("Even Numbers: ", even_numbers)
print("Odd Numbers: ", odd_numbers)
