#1
# from itertools import *

# c = 0
# for i in product(range(4), repeat=3):
#     if (i[0] + i[2] > i[1]) and i[0] != 0:
#         c += 1
# print(c)


#2
# from itertools import *

# c = 0
# for i in product("1234", repeat=5):
#     if i.count("1") == 2:
#         c += 1
# print(c)


#3
# from itertools import *

# c = 0
# for i in permutations(range(7), r=4):
#     if (i[0] > i[1] > i[2] > i[3]) and i[0] != 0:
#         c += 1
# print(c)


#4
# from itertools import *

# c = 0
# for i in permutations(range(9), r=5):
#     if i[0] > i[1] > i[2] > i[3] > i[4]:
#         c += 1
# print(c)


#5
# from itertools import *

# c = 0
# for i in product(range(9), repeat=5):
#     if i[0] != 0 and i.count(5) == 1:
#         if i[0] != 5 and i[-1] != 5:
#             if i[i.index(5) - 1] % 2 == 0 and i[i.index(5) + 1] % 2 == 0:
#                 c += 1
#         if i[0] == 5: 
#             c += i[i.index(5) + 1] % 2 == 0
#         if i[-1] == 5:
#             c += i[i.index(5) - 1] % 2 == 0
                
# print(c)


#6
# from itertools import *

# c = 0
# for i in product("ABCDEFX", repeat=4):
#     if i.count("X") == 1:
#         c += 1
# print(c)


#7
# from itertools import *

# c = 0
# for i in product("ABCDEX", repeat=4):
#     if i.count("X") == 1:
#         c += 1
# print(c)


#8
# from itertools import *

# c = 0
# for i in product("ABCDXYZ", repeat=4):
#     if (i[0] == "X" and i.count("X") == 1 and i.count("Y") == 0 and i.count("Z") == 0) or \
#         (i[0] == "Y" and i.count("Y") == 1 and i.count("X") == 0 and i.count("Z") == 0) or \
#         (i[0] == "Z" and i.count("Z") == 1 and i.count("Y") == 0 and i.count("X") == 0):
#          c += 1
# print(c)


#9
# from itertools import *

# c = 0
# for i in product("ABCDEF", repeat=5):
#     if i[0] != "F" and i[-1] != "A":
#         c += 1
# print(c)


#10
# from itertools import *

# c = 0
# for i in product("ABCDXYZ", repeat=4):
#     if i[0] in "XYZ" and i[1] in "XYZ" and i[0] not in "ABCD" and i[1] not in "ABCD" \
#     and i[2] not in "XYZ" and i[3] not in "XYZ" and i[2] in "ABCD" and i[3] in "ABCD":
#         c += 1
# print(c)


#11
# from itertools import *

# c = 0
# for i in permutations("ГЕРАСИМ", r=7):
#     # if i[0] in "ЕАИ" != i[1] in "ЕАИ" != i[2] in "ЕАИ" != i[3] in "ЕАИ" != i[4] in "ЕАИ" != i[5] in "ЕАИ" != i[6] in "ЕАИ":
#     if (i[0] in "ЕАИ" and i[1] in "ГРСМ" and i[2] in "ЕАИ" and i[3] in "ГРСМ" and i[4] in "ЕАИ" and i[5] in "ГРСМ" and i[6] in "ЕАИ") \
#         or (i[0] in "ГРСМ" and i[1] in "ЕАИ" and i[2] in "ГРСМ" and i[3] in "ЕАИ" and i[4] in "ГРСМ" and i[5] in "ЕАИ" and i[6] in "ГРСМ"):
#         c += 1
# print(c)


#12
# from itertools import *

# c = 0
# for i in product("ИВАН", repeat=5):
#     if i.count("И") > 0:
#         c += 1
# print(c)