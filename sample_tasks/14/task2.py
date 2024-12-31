n =  12 * 7**135 + 11 * 7**92 - 63 * 7**22 + 17 * 7**11 + 157
lst = []
while n > 0:
    lst.append(n % 7)
    n = n // 7
print(len(set(lst)))