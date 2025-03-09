#1
# !!! i[0] != 0
# from itertools import *

# c = 0
# for i in product(range(12), repeat=5):
#     if i[0] != 0 and i.count(7) == 1 and (i.count(9) + i.count(10) + i.count(11)) < 4:
#         c += 1
# print(c)


#2
# !!! i[0] != 0
# from itertools import *

# c = 0
# for i in product(range(14), repeat=5):
#     if i[0] != 0 and i.count(9) == 1 and (i.count(11) + i.count(12) + i.count(13)) < 4:
#         c += 1
# print(c)


#2 type
#3
# from itertools import *

# p = 1
# for i in product("АКРУ", repeat=5):
#     s = "".join(i)
#     if p == 350:
#         print(p, s)
#     p += 1


#4
# from itertools import *

# p = 1
# for i in product("АОУ", repeat=5):
#     s = "".join(i)
#     if s == "УАУАУ":
#         print(p, s)
#     p += 1


#5
# from itertools import *

# p = 1
# for i in product("ДЕКОР", repeat=4):
#     s = "".join(i)
#     if s[0] == "К":
#         print(p, s)
#         break
#     p += 1


#6 (ЕГЭ 2024)
# from itertools import *

# p = 1
# for i in product("АПРСУ", repeat=5):
#     s = "".join(i)
#     if s[0] == "У" and "АА" not in s:
#         print(p, s)
#         break
#     p += 1


#7 (ЕГЭ 2024)
# from itertools import *

# p = 1
# for i in product("КОСУФ", repeat=5):
#     s = "".join(i)
#     if s.count("Ф") == 0 and s.count("У") == 2:
#         print(p, s)
#     p += 1


#8
# from itertools import *

# p = 1
# lst = []
# for i in product("АИКМНОПЯ", repeat=6):
#     s = "".join(i)
#     if p % 2 != 0 and s[0] != "М" and s.count("И") == 3:
#         lst.append(s)
#     p += 1
# print(len(lst))


#9
# from itertools import *

# c = 0
# p = 1
# for i in product("ЬРПЛЕА", repeat=5):
#     s = "".join(i)
#     if s[-1] == "Ь" and p < 388:
#         c += 1
#     p += 1
# print(c)


#10 из апробации 
# from itertools import *

# c = 0
# for i in product(range(9), repeat=5):
#     if i[0] != 0 and i.count(0) == 1:
#         if i[-1] != 0:
#             if i[i.index(0) - 1] % 2 == 0 and i[i.index(0) + 1] % 2 == 0:
#                 c += 1
#         else:
#             if i[i.index(0) - 1] % 2 == 0:
#                 c += 1
# print(c)