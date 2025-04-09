#1
# from itertools import *

# c = 0
# lst = []
# for i in product("АЕПСТУХ", repeat=4):
#     s = "".join(i)
#     c += 1
#     if "АА" not in s and "ЕЕ" not in s and "ПП" not in s and "СС" not in s \
#         and "ТТ" not in s and "УУ" not in s and "ХХ" not in s and c > 1000:
#             lst.append(s)
# print(len(lst))
    

#2
# from itertools import *

# c = 1
# for i in product("АПРСУ", repeat=5):
#     s = "".join(i)
#     c += 1
#     if s[0] == "У" and "АА" not in s:
#         print(c, s)
#         break


#3
# from itertools import *

# c = 0
# for i in product(range(5), repeat=5):
#     if i[0] != 0 and (i.count(0) + i.count(2) + i.count(4)) < 4:
#         c += 1
# print(c)


#4
# from itertools import *

# c = 0
# for i in permutations("СОТКАПЛЗ", r=5):
#     s = "".join(i)
#     if s[-1] not in "ОА" and "ЗЛО" not in s:
#         c += 1
# print(c)


#5
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#6
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x or (not y)) and (not(x == z)) and (not w)
#                 if f == 1:
#                     print(x, y, z, w)


#7
# for n in range(4, 10000):
#     s = "1" + "2" * n
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "322" in s:
#             s = s.replace("322", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "3", 1)
#     su = sum([int(x) for x in s])
#     if su == 15:
#         print(n)
#         break