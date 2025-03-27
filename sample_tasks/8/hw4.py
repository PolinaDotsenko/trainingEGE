#1
# from itertools import *

# p = 1
# for i in product("АОУ", repeat=5):
#     if i[0] == "У":
#         print(p, i)
#         break
#     p += 1


#2
# from itertools import *

# p = 1
# for i in product("АКРУ", repeat=5):
#     if i[0] == "К":
#         print(p, i)
#         break
#     p += 1


#3
# from itertools import *

# p = 1
# for i in product("АКРУ", repeat=5):
#     s = "".join(i)
#     if p == 250:
#         print(p, s)
#     p += 1


#4
# from itertools import *

# p = 1
# for i in product("АКРУ", repeat=5):
#     s = "".join(i)
#     if p == 450:
#         print(p, s)
#     p += 1


#5
# from itertools import *

# p = 1
# for i in product("ЕКМОПРТЬ", repeat=5):
#     s = "".join(i)
#     if s.count("К") == 0 and s.count("Р") == 2:
#         print(p, s)
#     p += 1


#6
# from itertools import *

# p = 1
# for i in product("АПРСУ", repeat=5):
#     s = "".join(i)
#     if s.count("У") < 2 and "АА" not in s:
#         print(p, s)
#     p += 1


#7
# from itertools import *

# p = 1
# for i in product("АВЕСТ", repeat=5):
#     s = "".join(i)
#     if s == "СВЕТА":
#         print(p, s)
#     p += 1


#8
# from itertools import *

# p = 1
# for i in product("АГМНСТУ", repeat=6): 
#     s = "".join(i)
#     if s[0] != "У" and s.count("М") == 2 and s.count("Г") < 2:
#         print(p, s)
#     p += 1


#9
# from itertools import *

# p = 1
# for i in product("АВОРТ", repeat=4):
#     s = "".join(i)
#     if s == "ВАТА":
#         print(p, s)
#     p += 1


#10
from itertools import *

p = 1
for i in product("АПРСУ", repeat=3):
    if i[0] == "Р":
        print(p)
        break
    p += 1