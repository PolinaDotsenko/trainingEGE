#комбинаторика. 1 тип 
#1
# from itertools import product

# c = 0
# for i in product("ГОД", repeat=6):
#     if i[0] in "ГД" and i[-1] in "ГД":
#         c += 1
# print(c)


#2 
# from itertools import *

# c = 0
# for i in product("МЕТРО", repeat=4):
#     if i[0] in "МТР" and i[3] in "ЕО":
#         c += 1
# print(c)


#3
# from itertools import *

# c = 0
# for i in product("ABCX", repeat=5):
#     if (i[0] in "X" and i.count("X") == 1) or (i.count("X") == 0):
#         c += 1
# print(c)


#4
# from itertools import *

# c = 0
# for i in product("ABCX", repeat=5):
#     if i.count("X") == 1:
#         c += 1
# print(c)


#5
# from itertools import *

# c = 0
# for i in product("ABCDXYZ", repeat=4):
#     if i[0] in "XYZ" and i[1] not in "XYZ" \
#         and i[2] not in "XYZ" and i[3] not in "XYZ":
#         c += 1
# print(c)


#6
# from itertools import *

# lst = []
# for i in product("ОГЭИНФ", repeat=6):
#     s = "".join(i)
#     if s[0] in "ЭО" and s[-2:] == "НФ" \
#         and s.count("ИГ") > 0 and s.count("ОГЭ") == 0:
#         lst.append(s)
# print(len(lst))


#7
# from itertools import *

# lst = []
# for i in permutations("СОТКАПЛЗ", r=5):
#     s = "".join(i)
#     if s[-1] not in "ОА" and "ЗЛО" not in s:
#         lst.append(s)
# print(len(lst))


#9 перестановка букв == permutations
# from itertools import *

# lst = []
# for i in permutations("ТИКТОК"):
#     s = "".join(i)
#     if s[0] != s[1] != s[2] != s[3] != s[4] != s[5]:
#         lst.append(s)
# print(len(set(lst)))  #из-за повторяющихся букв пишем set()