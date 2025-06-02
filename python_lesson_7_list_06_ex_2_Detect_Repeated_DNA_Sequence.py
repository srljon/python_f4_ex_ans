dna_segments = [12, 15, 18, 15, 20]
found_repeat = False
i = 0

while i < len(dna_segments) and found_repeat == False:
    j = i + 1
    while j < len(dna_segments) and found_repeat == False:
        if dna_segments[i] == dna_segments[j]:
            print(dna_segments[i])
            found_repeat == True
        j += 1
    i += 1
