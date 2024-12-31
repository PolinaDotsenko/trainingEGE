n = 9**81 + 27**729 - 4
lst = []
while n > 0:
    lst.append(n % 9)
    n = n // 9
s = [max(lst) if i == 0 else i for i in lst]
print(s.count(max(s)))