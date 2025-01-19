#2
# f = open("sample_tasks\\17\\files_pr1\\17-257.txt")
# lst = [int(x) for x in f]
# chet = [x for x in lst if x % 2 == 0]
# nechet = [x for x in lst if x % 2 != 0]
# if max(chet) > max(nechet):
#     print(len(chet), min(chet))
# else:
#     print(len(nechet), min(nechet))


#3
# f = open("sample_tasks\\17\\files_pr1\\17-1.txt")
# lst = [int(x) for x in f]
# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a % 7 == 0 and b % 17 != 0) or (b % 7 == 0 and a % 17 != 0):
#         ans.append(a + b)
# print(len(ans), min(ans))


#4
# f = open("sample_tasks\\17\\files_pr1\\17-345.txt")
# lst = [int(x) for x in f]
# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a < max(lst) - min(lst)) + (b < max(lst) - min(lst)) == 1:
#         ans.append(a + b)
# print(len(ans), max(ans))


#5
# f = open("C:\\VSCodeProjects\\trainingEGE\\sample_tasks\\17\\files_pr1\\17-336.txt")
# lst = [int(x) for x in f]
# m = max([x for x in lst if x % 37 == 0])
# ans = []
# for i in range(len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if a % m == 0 or b % m == 0:
#         ans.append(a + b)
# print(len(ans), min(ans))


#6
# f = open("sample_tasks\\17\\files_pr1\\17-1.txt")
# lst = [int(x) for x in f]
# ind = []
# s = []
# for i in range(1, len(lst) - 1):
#     a, b, c = lst[i - 1], lst[i], lst[i + 1]
#     if b > a and b > c:
#         ind.append(i)
# for x in range(1, len(ind) - 1):
#     s.append(ind[x] - ind[x - 1])
# print(len(ind), min(s))


#7 егэ2024
f = open("sample_tasks\\17\\files_pr1\\17-409.txt")
lst = [int(x) for x in f]
k7 = [x for x in lst if abs(x) % 10 == 7 and (1000 <= abs(x) <= 9999)]
ans = []
for i in range(0, len(lst) - 2):
    a, b, c = lst[i], lst[i + 1], lst[i + 2]
    if (a in k7) + (b in k7) + (c in k7) > 1:
        if a + b + c > max(k7):
            ans.append(a + b + c)
print(len(ans), max(ans))