lst = []
for i in range(0, 100):
    n = bin(i)[2:]
    n += str(int(n.count("1")) % 2)
    n += str(int(n.count("1")) % 2)
    r = int(n, 2)
    if r < 50:
        lst.append(r)

print(max(lst))