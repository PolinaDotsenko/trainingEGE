for i in range(2, 1500):
    N = i
    n = bin(N)[2:-1]
    if N % 2 == 0:
        n += "01"
    else:
        n += "10"
    r = int(n, 2)
    if r == 2017:
        print(r)
        print(i)
        break
