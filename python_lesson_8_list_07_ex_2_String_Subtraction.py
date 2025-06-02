str1 = "hello"
str2 = "world"
result = ""

i = 0
while i < len(str1):
    j = 0
    found = False  # Flag to indicate if str1[i] is found in str2

    while j < len(str2):
        if str1[i] == str2[j]:
            found = True
            break  # Exit inner loop as match is found
        j += 1

    if not found:
        result += str1[i]  # Append str1[i] to result if not found in str2

    i += 1

print("Result:", result)  # Expected output: "he"
