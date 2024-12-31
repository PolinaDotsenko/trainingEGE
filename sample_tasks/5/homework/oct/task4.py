f = open("17-(2).txt")
lst = [int(x) for x in f]
count = 0
res = []
for i in range(0, len(lst) - 1):
    a, b = lst[i], lst[i + 1]
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        count += 1
        res.append(a + b)
print(count, max(res))