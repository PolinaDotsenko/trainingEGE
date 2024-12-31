lst = []
for i in range(1000, 10000):
    n1 = str(int(str(i)[0]) + int(str(i)[1]))
    n2 = str(int(str(i)[2]) + int(str(i)[3]))
    r = max(n1, n2) + min(n1, n2)
    if r == "1311":
        lst.append(i)

print(min(lst))