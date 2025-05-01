#1
# from itertools import *

# def f(x):
#     p = 5 <= x <= 30
#     q = 14 <= x <= 23
#     a = a1 <= x <= a2
#     return (p == q) <= (not a)

# ox = [i / 4 for i in range(4*4, 31*4)]    #берем отрезок чуть больше
# lst = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#2
# from itertools import *

# def f(x):
#     p = 10 <= x <= 29
#     q = 13 <= x <= 18
#     a = a1 <= x <= a2
#     return (a <= p) or q

# ox = [i / 4 for i in range(9*4, 30*4)]
# lst = []
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#3
# from itertools import *

# def f(x):
#     p = 4 <= x <= 15
#     q = 12 <= x <= 20
#     a = a1 <= x <= a2
#     return (p and q) <= a

# lst = []
# ox = [i / 4 for i in range(3*4, 21*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#4
# from itertools import *

# def f(x):
#     p = 130 <= x <= 171
#     q = 150 <= x <= 185
#     a = a1 <= x <= a2
#     return p <= ((q and (not a)) <= (not p))

# lst = []
# ox = [i / 4 for i in range(129*4, 186*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#5
# from itertools import *

# def f(x):
#     p = 20 <= x <= 50
#     q = 30 <= x <= 65
#     a = a1 <= x <= a2
#     return (not a) <= (p <= (not q))

# lst = []
# ox = [i / 4 for i in range(19*4, 66*4)] 
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#6
# from itertools import *

# def f(x):
#     p = 17 <= x <= 46
#     q = 22 <= x <= 57
#     a = a1 <= x <= a2
#     return (not a) <= ((p and q) <= a)

# lst = []
# ox = [i / 4 for i in range(16*4, 58*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#7
from itertools import *

def f(x):
    p = 17 <= x <= 40
    q = 20 <= x <= 57
    a = a1 <= x <= a2
    return (not a) <= ((p and q) <= a)

lst = []
ox = [i / 4 for i in range(16*4, 58*4)]
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        lst.append(a2 - a1)
print(min(lst))


#8
# from itertools import *

# def f(x):
#     p = 10 <= x <= 40
#     q = 5 <= x <= 15
#     r = 35 <= x <= 50
#     a = a1 <= x <= a2
#     return (a or p) or (q <= r)

# lst = []
# ox = [i / 4 for i in range(4*4, 51*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#9  комбинированное из егэ прошлого года
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     b = 70 <= x <= 90
#     return d(x, a) or (b <= (not d(x, 27)))

# for a in range(1, 1000):
#     if all(f(a, x) == 1 for x in range(1, 1000)):
#             print(a)