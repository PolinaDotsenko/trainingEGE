#1 type
#1
# from itertools import *
#
# c = 0
# for i in product("ШКОЛА", repeat=3):
#     if i.count("К") == 1:
#         c += 1
# print(c)


#2
# from itertools import *
#
# c = 0
# for i in product("ABCX", repeat=5):
#     if (i[0] == "X" and i.count("X") == 1) or i.count("X") == 0:
#         c += 1
# print(c)


#3
# from itertools import *
#
# c = 0
# for i in product(range(16), repeat=5):
#     if i[-1] % 2 != 0 and i[0] != 1 and i[0] != 0:  #!!!i.count("X") == 0!!!
#         c += 1
# print(c)


#4
# from itertools import *
#
# c = 0
# for i in permutations(range(8), r=5):
#     if i[0] != 0 and i.count(1) == 0:
#         if i[0] % 2 != i[1] % 2 != i[2] % 2 != i[3] % 2 != i[4] % 2:
#             c += 1
# print(c)


#5
# from itertools import *
#
# c = 0
# for i in product("ABCDXYZ", repeat=4):
#     if (i[0] == "X" and i.count("X") == 1 and i.count("Y") == 0 and i.count("Z") == 0) or \
#             (i[0] == "Y" and i.count("Y") == 1 and i.count("X") == 0 and i.count("Z") == 0) or\
#                     (i[0] == "Z" and i.count("Z") == 1 and i.count("Y") == 0 and i.count("X") == 0):
#         c += 1
# print(c)


#6
# from itertools import *
#
# c = 0
# for i in product("ОГЭИНФ", repeat=6):
#     s = "".join(i)
#     if s[0] in "ЭО" and s[-2:] == "НФ" and "ИГ" in s and "ОГЭ" not in s:
#         c += 1
# print(c)


#7
# from itertools import *
#
# c = 0
# for i in permutations("СОТКАПЛЗ", r=5):
#     s = "".join(i)
#     if s[-1] not in "ОА" and "ЗЛО" not in s:
#         c += 1
# print(c)


#9 !!!
# from itertools import *
#
# lst = []
# for i in permutations("ТИКТОК"):
#     if i[0] != i[1] != i[2] != i[3] != i[4] != i[5]:
#         lst.append(i)
# print(len(set(lst)))