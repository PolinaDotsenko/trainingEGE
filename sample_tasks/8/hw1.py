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
# print(c)