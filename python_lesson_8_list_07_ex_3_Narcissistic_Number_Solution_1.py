# Narcissistic number
num_check = 100
a = 0
b = 0
c = 0

while num_check <= 999:
    a = str(num_check)[0]
    b = str(num_check)[1]
    c = str(num_check)[2]
    # a = num_check // 100          # Hundreds digit
    # b = (num_check // 10) % 10    # Tens digit
    # c = num_check % 10            # Ones digit

    total = int(a)**3 + int(b)**3 + int(c)**3
    # print(total)
    if num_check == total:
        print(f"{total} \u2192 {a}\u00B3 + {b}\u00B3 + {c}\u00B3 = {total} (3-digit example)")
        # "1³", "1\u00B3", "1\N{SUPERSCRIPT THREE}"
        # "→", "\u2192", "\N{RIGHTWARDS ARROW}"
    num_check += 1
