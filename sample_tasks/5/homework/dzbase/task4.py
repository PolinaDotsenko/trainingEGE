for i in range(0, 256):
    n = bin(i)[2:].zfill(8)
    s = ""
    for j in n:
        if j == "1":
            s += "0"
        else:
            s += "1"
    r = int(s, 2)
    if r - i == 111:
        print(r - i)
        print(i)
        break