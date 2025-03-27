from itertools import *

p = 1
for i in product("АПРСУ", repeat=3):
    if i[0] == "Р":
        print(p)
        break
    p += 1