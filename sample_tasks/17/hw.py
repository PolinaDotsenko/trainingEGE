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
# f = open("sample_tasks\\17\\17-3.txt")
# lst = [int(x) for x in f]
# ans = []
# for i in range(1, len(lst) - 4):
#     a, b, c, d = lst[i], lst[i +1], lst[i + 2], lst[i +3]
#     if (lst[i - 1] % 2) + (lst[i +  4] % 2) == 1:
#         ans.append(a + b + c + d)
# print(len(ans), max(ans))


#3
# def convert(num, base):
#     lst = []
#     while num > 0:
#         lst.append(num % base)
#         num = num // base
#     lst = [str(x) for x in lst[::-1]]
#     return "".join(lst)
    

# f = open("sample_tasks\\17\\17-4.txt")
# lst = [int(x) for x in f]
# ans = []
# for i in lst:
#     n = str(bin(i)[2:])
#     if n[-4:] == "1001" and convert(i, 5)[-2::] == "11":
#         ans.append(i)
# ans = [int(x) for x in ans]
# print(max(ans), sum(ans))


#4
# def convert(num, base):
#     lst = []
#     while num > 0:
#         lst.append(num % base)
#         num = num // base
#     lst = [str(x) for x in lst[::-1]]
#     return "".join(lst)


# f = open("sample_tasks\\17\\17-4.txt")
# lst = [int(x) for x in f]
# ans = []
# for i in lst:
#     if convert(i, 5)[-1::] == "3" and convert(i, 9)[-1::] == "5" and convert(i, 8)[-1::] != "7":
#         ans.append(i)
# print(len(ans), max(ans))


#5
# f = open("sample_tasks\\17\\17-1.txt")
# lst = [int(x) for x in f]
# ans = []
# avrg = sum(lst) / len(lst)
# for i in range(0, len(lst) - 2):
#     a, b, c = lst[i], lst[i + 1], lst[i + 2]
#     if ((a < avrg) + (b < avrg) + (c < avrg) > 0) \
#         and ((abs(a) % 10 == 4) + (abs(b) % 10 == 4) + (abs(c) % 10 == 4) > 1):
#         ans.append(a + b + c)
# print(len(ans), max(ans))