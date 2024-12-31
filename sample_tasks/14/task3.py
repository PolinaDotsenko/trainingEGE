n = 5 * 216**1256 - 5 * 36**1146 + 4 * 6**1053 - 1087
lst = []
while n > 0:
    lst.append(n % 6)
    n = n // 6
print(sum(lst))