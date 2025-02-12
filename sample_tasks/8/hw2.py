#1      base
# from itertools import *

# k = 1
# for i in product("ВИНТ", repeat=5):
#     s = "".join(i)
#     if k == 1020:
#         print(s)
#     k += 1


#2
# from itertools import *

# k = 1
# for i in product("БКФ", repeat=6):
#     s = "".join(i)
#     if k == 345:
#         print(s)
#     k += 1


#3
# from itertools import *

# k = 1
# for i in product("ЕЖИ", repeat=5):
#     s = "".join(i)
#     if k == 238:
#         print(s)
#     k += 1


#4
# from itertools import *

# k = 1
# for i in product("АМУХ", repeat=4):
#     s = "".join(i)
#     if s == "ХУХХ":
#         print(k)
#     k += 1


#5
# from itertools import *

# k = 1
# for i in product("ВЕКНО", repeat=5):
#     s = "".join(i)
#     if s[0] == "О":
#         print(k)
#         break
#     k += 1


#6
# from itertools import *

# k = 1
# for i in product("ВЕСТ", repeat=6):
#     s = "".join(i)
#     if s[0] == "Т":
#         print(k)
#         break
#     k += 1


#1      pro
# from itertools import * 
# c = 1 
# for i in product('ПОРТ', repeat=5): 
#     s = ''.join(i) 
#     if s == 'ТОПОР' or s == 'РОПОТ': 
#         print(c)
#     c += 1
# print(839 - 584 + 1)


#2
# from itertools import *

# k = 1
# for i in product("АЗНС", repeat=5):
#     s = "".join(i)
#     if s == "САЗАН" or s == "ЗАНАС":
#         print(k)
#     k += 1
# print(787 - 292 + 1)


#3
# from itertools import *

# k = 1
# for i in product("ЁИКЛНОС", repeat=5):
#     s = "".join(i)
#     if s.count("Ё") > 1 and s[0] != "О" and s[1] == "К":
#         print(k, s)
#     k += 1