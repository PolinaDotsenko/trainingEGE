for i in range(0, 100):
    N = i
    n = bin(N - (N % 4))[2:]
    n = n + (str(n.count("1") % 2))
    n = n + (str(n.count("1") % 2))
    r = int(n, 2)
    if r < 47:
        print(i)