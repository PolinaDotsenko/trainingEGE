#1
# f = open("sample_tasks\\17\\files_pr2\\17-257.txt")
# lst = [int(x) for x in f]
# k11 = [x for x in lst if x % 11 == 0]
# k17 = [x for x in lst if x % 17 == 0]
# if len(k11) > len(k17):
#     print(len(k11), min(k11))
# else:
#     print(len(k17), max(k17))


#2
# f = open("sample_tasks\\17\\files_pr2\\17-432.txt")
# lst = [int(x) for x in f]
# su_n = sum(x for x in lst if x < 0)

# ans = []
# for i in range(1, len(lst) - 1):
#     a = [lst[i - 1], lst[i], lst[i + 1]]
#     if max(a) * min(a) > su_n:
#         ans.append(sum(a))
# print(len(ans), abs(max(ans)))


#3
# f = open("sample_tasks\\17\\files_pr2\\17-1.txt")
# lst = [int(x) for x in f]

# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a % 7 == 0 and b % 17 != 0) or (b % 7 == 0 and a % 17 != 0):
#         ans.append(a + b)
# print(len(ans), min(ans))


#4
# f = open("sample_tasks\\17\\files_pr2\\17-345.txt")
# lst = [int(x) for x in f]
# r = max(lst) - min(lst)

# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if ((a < r) + (b < r)) == 1:
#         ans.append(a + b)
# print(len(ans), max(ans))


#5
# f = open("sample_tasks\\17\\files_pr2\\17-336.txt")
# lst = [int(x) for x in f]
# m = max(x for x in lst if x % 37 == 0)

# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if a % m == 0 or b % m == 0:
#         ans.append(a + b)
# print(len(ans), min(ans))


#6
# f = open("sample_tasks\\17\\files_pr2\\17-390.txt")
# lst = [int(x) for x in f]
# k38 = [x for x in lst if abs(x) % 100 == 38]
# sr = sum(k38) / len(k38)

# ans = []
# for i in range(0, len(lst) - 2):
#     a, b, c = lst[i], lst[i + 1], lst[i + 2]
#     if ((100 <= abs(a) <= 999) + (100 <= abs(b) <= 999) + (100 <= abs(c) <= 999)) >= 2:
#         if (abs(a) % 10 == 3) + (abs(b) % 10 == 3) + (abs(c) % 10 == 3) == 1:
#             if a < sr and b < sr and c < sr:
#                 ans.append(a + b + c)
# print(len(ans), max(ans))