lst = []
for i in range(0, 100):  
    N = i
    n = bin(N)[2:]
    if n.count("1") > n.count("0"):
        n += "1"
    else:
        n += "0"
    r = int(n, 2)
    if r < 100:
        lst.append(r)
print(max(lst))