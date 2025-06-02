#17 старые
#1
# c = 0
# for i in range(3439, 7411):
#     if i % 9 == 0 or i % 10 == 0 or i % 11 == 0:
#         if i % 2 != i % 6:
#             c += 1
# print(c)

#2
# lst = []
# for i in range(3**7, 3**8):
#     if i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
#         lst.append(i)
# print(sum(lst))


#3
# lst = []
# for i in range(2738, 7515):
#     if i % 7 == 0 and i % 19 != 0:
#         lst.append(i)
# print(len(lst), sum(lst))


#17 актуальные
#1
# res = []
# f = open("17-1.txt")
# lst = [int(x) for x in f]
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if a % 3 == 0 or b % 3 == 0:
#         res.append(a + b)
# print(len(res), max(res))


#2
# f = open("17-1.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if (str(a)[-1] == "6" and a % 3 == 0) or (str(b)[-1] == "6" and b % 3 == 0):
#         res.append(min(a, b))
# print(len(res), min(res))


#3
# f = open("17-2.txt")
# lst = [int(x) for x in f]
# print(lst.count(max(lst)), lst.index(max(lst)) + 1)


#4
# f = open("17-4.txt")
# lst = [int(x) for x in f]
# avr = sum(lst) / len(lst)
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if a < avr and b < avr and (str(a)[-1] == "9" or str(b)[-1] == "9"):
#         res.append(a + b)
# print(len(res), max(res))


#5 досрок
