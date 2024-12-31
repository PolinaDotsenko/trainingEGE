for x in range(0, 22):
    a = f"7{x}38596"
    b = f"14{x}36"
    c = f"61{x}7"
    res = int(a, 23) + int(b, 23) + int(c, 23)
    if res % 22 == 0:
        print(res / 22)