#1
# f = open("sample_tasks\\17\\17__1a3zm.txt")
# lst = [int(x) for x in f]
# avrg = sum(lst) / len(lst)
# ans = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a < avrg and b < avrg) and ((a + b) % 100 == 19):
#         ans.append(a + b)
# print(len(ans), min(ans))


#2
f = open("sample_tasks\\17\\17-3.txt")
lst = [int(x) for x in f]
for i in range(1, len(lst) - 4):
    a, b, c, d = lst[i], lst[i +1], lst[i + 2], lst[i +3]