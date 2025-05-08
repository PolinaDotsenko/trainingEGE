#1
# f = open("sample_tasks\\17\\17-3.txt")
# lst = [int(x) for x in f]

# ans = []
# for i in range(0, len(lst) - 2):
#     a = [lst[i], lst[i + 1], lst[i + 2]]
#     p = a[0] * a[1] * a[2]
#     su = sum(a)
#     if p % 7 == 0:
#         if abs(su) % 10 == 5:
#             ans.append(su)
# print(len(ans), max(ans))


#2
# f = open("sample_tasks\\17\\17-1.txt")
# lst = [int(x) for x in f]

# res = []
# for i in range(1, len(lst) - 1):
#     a = [lst[i - 1], lst[i], lst[i + 1]]
#     if lst[i - 1] > lst[i] < lst[i + 1]:
#         res.append(lst[i])
# print(len(res), max(res))


#3
# f = open("sample_tasks\\17\\17-1.txt")
# lst = [int(x) for x in f]

# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if a < b:
#         res.append(abs(a - b))
# print(len(res), min(res))


#4
f = open("sample_tasks\\17\\17-1.txt")
lst = [int(x) for x in f]

res = []
for i in range(0, len(lst) - 1):
    a, b = lst[i], lst[i + 1]
    if (a % 9 == 0 and oct(b)[-1] == "3" and b % 9 != 0) or \
        (b % 9 == 0 and oct(a)[-1] == "3" and a % 9 != 0):
        res.append(max(a, b))
print(len(res), max(res))