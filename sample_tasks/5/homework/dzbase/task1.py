for i in range(1, 100):   
    N = i
    n = bin(N)[2:]
    if N % 2 == 0:
        n += "01"
    else:
        n += "10"
    r = int(n, 2)
    if r > 102:
        print(r)
        break