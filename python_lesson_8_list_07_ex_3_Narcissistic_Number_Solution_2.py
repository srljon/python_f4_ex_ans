# Narcissistic number 2
a = 1
while a < 10:
    b = 0
    while b < 10:
        c = 0
        while c < 10:
            total = a*100 + b*10 + c
            if a**3 + b**3 + c**3 == total:
                print(f"{total} \u2192 {a}\u00B3 + {b}\u00B3 + {c}\u00B3 = {total} (3-digit example)")
            c += 1
        b += 1
    a += 1
