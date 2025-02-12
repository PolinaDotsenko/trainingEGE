#1      base
# from itertools import *

# c = 0
# for i in product("ПИКАЧУ", repeat=5):
#     if i.count("У") >= 2:
#         c += 1
# print(c)


#2
# from itertools import *

# c = 0
# for i in permutations("ВАЙФУ", r=4):
#     s = "".join(i)
#     if s[0] != "Й" and s.count("ВФ") == 0 and s.count("ФВ") == 0:
#         c += 1
# print(c)


#3
# from itertools import *

# lst = []
# for i in permutations("КЛАБХАУС"):
#     s = "".join(i)
#     if s[0] != s[1] != s[2] != s[3] != s[4] != s[5] != s[6] != s[7]:
#         lst.append(s)
# print(len(set(lst)))
    

#4
# from itertools import *

# c = 0
# for i in product("ABCX", repeat=5):
#     if i.count("X") == 1 and (i[0] == "X" or i[-1] == "X"):
#         c += 1
# print(c)


#5
# from itertools import *

# c = 0
# for i in product("ABX", repeat=6):
#     if i.count("X") == 1:
#         c += 1
# print(c)


#6
# from itertools import *

# c = 0
# for i in product("ABCDEF", repeat=5):
#     if i[0] != "F" and i[-1] != "A":
#         c += 1
#print(c)


#1      pro
# from itertools import *

# lst = []
# for i in product("МЕЧТА", repeat=6):
#     s = "".join(i)
#     if s.count("А") > 2:
#         lst.append(s)
# print(len(lst))


#2
# from itertools import *

# lst = []
# for i in permutations("АВТОМАТ", r=7):
#     s = "".join(i)
#     a = "АОА"
#     b = "ВТМТ"
#     if (s[0] in a and s[1] in b and s[2] in a and s[3] in b and s[4] in a and s[5] in b and s[6] in a) \
#         or (s[0] in b and s[1] in a and s[2] in b and s[3] in a and s[4] in b and s[5] in a and s[6] in b):
#             lst.append(s)
# print(len(set(lst)))


#3
# from itertools import *

# lst = []
# for i in product("ЕГЭИНФ", repeat=6):
#     s = "".join(i)
#     if s[0] == "Е" and s[-1] in "ЭИ" \
#         and s.count("ФИ") > 1 and "ЕГЭ" not in s:
#             lst.append(s)
# print(len(lst))


#4
# from itertools import *

# lst = []
# for i in product("ОБЩЕСТВ", repeat=5):
#     s = "".join(i)
#     if s[0] not in "ЩБ" and s[-2:] == "ВВ" \
#         and "ЕВ" not in s and "ВЕ" not in s and s.count("ТБ") > 0:
#         lst.append(s)
# print(len(lst))