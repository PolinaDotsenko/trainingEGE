#1
# from itertools import *

# lst = []
# for i in product(range(12), repeat=5):
#     if i[0] !i[0] != 0 and i.count(7) == 1 and sorted(i)[-4] <= 8:    
# !  i[0] != 0 если в начале ноль, то число не пятизначное
# TODO  don't forget using sorted()
#         lst.append(i)
# print(len(lst))


#2
# from itertools import *

# lst = []
# for i in product(range(14), repeat=5):
#     if i[0] != 0 and i.count(9) == 1 and sorted(i)[-4] < 11:
#         lst.append(i)
# print(len(lst))


#3
#*  другой прототип
#TODO надо проверять порядок букв в условии 
# from itertools import *

# k = 1
# for i in product("АКРУ", repeat=5):
#     s = "".join(i)
#     if k == 350:
#         print(s)
#     k += 1
    

#4
# from itertools import *

# k = 1
# for i in product("АОУ", repeat=5):
#     s = "".join(i)
#     if s == "УАУАУ":
#         print(k)
#     k += 1


#5
# from itertools import *

# k = 1
# for i in product("АКРУ", repeat=5):
#     if i[0] == "У":
#         print(k)
#         break
#     k += 1


#6
# from itertools import *

# k = 1
# for i in product("АПРСУ", repeat=5):
#     s = "".join(i)
#     if s[0] == "У" and "АА" not in s:
#         print(k) 
#         break
#     k += 1


#7
# from itertools import *

# k = 1
# for i in product("КОСУФ", repeat=5):
#     s = "".join(i)
#     if s.count("Ф") == 0 and s.count("У") == 2:
#         print(str(k) + ".", s)
#     k += 1


#8
# from itertools import *

# lst = []
# k = 1
# for i in product("АИКМНОПЯ", repeat=6):
#     s = "".join(i)
#     if s[0] != "М" and s.count("И") == 3 and k % 2 != 0:
#         lst.append(s)
#     k += 1
# print(len(lst))


#9
# from itertools import *

# k = 0
# for i in product("АКЛОШ", repeat=5):
#     s = "".join(i)
#     if "А" in s or "О" in s:
#         k += 1
# print(k)