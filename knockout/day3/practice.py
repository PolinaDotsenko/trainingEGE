#2
#1
# from itertools import *
#
# def f(x, y, z, w):
#     return x and (z <= w) and (not y)
#
# for i in product([0, 1], repeat=7):
#     table = [(i[0], i[1], 1, i[2]), (i[3], 1, 0, i[4]), (1, 0, i[5], i[6])]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
#                 print(p)


#2
# from itertools import *
#
# def f(x, y, z, w):
#     return ((x <= y) or (z == x)) and (w <= z)
#
# table = [(0, 0, 1, 1), (0, 0, 1, 0), (0, 1, 1, 1)]
# for p in permutations("xyzw"):
#     if [f(**dict(zip(p, r))) for r in table] == [1, 0, 0]:
#         print(p)


#3
# from itertools import *
#
# def f(x, y, z, w):
#     return ((x <= y) and (y <= w)) or (z == (x or y))
#
# for i in product([0, 1], repeat=7):
#     table = [(1, i[0], i[1], 1), (1, i[2], i[3], i[4]), (i[5], 1, i[6], 1)]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#                 print(p)


#5
#1
# res = []
# for i in range(0, 1000):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n = "1" + n + "10"
#     if i % 2 != 0:
#         n = "11" + n + "0"
#     r = int(n, 2)
#     if r in range(800, 1501):
#         res.append(r)
# print(len(set(res)))


#2
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     lst = [str(x) for x in lst]
#     res = "".join(lst[::-1])
#     return res
#
# ans = []
# for i in range(1, 1000):
#     n = convert(i, 4)
#     if i % 4 == 0:
#         n = n + n[-2:]  #!!!!!
#     if i % 4 != 0:
#         n = n + (convert((i % 4) * 5, 4))
#     r = int(n, 4)
#     if r < 555:
#         ans.append(i)
# print(max(ans))


#12
#1
# def isprime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True         #!!!!!!!
#
# for n in range(1, 300):
#     s = ">" + "0" * 39 + "1" * n + "2" * 39
#     while ">1" in s or ">2" in s or ">0" in s:
#         if ">1" in s:
#             s = s.replace(">1", "22>", 1)
#         if ">2" in s:
#             s = s.replace(">2", "2>", 1)
#         if ">0" in s:
#             s = s.replace(">0", "1>", 1)
#     s = s.replace(">", "0")
#     lst = sum([int(x) for x in s])
#     if isprime(lst):
#         print(n)
#         break


#теория игр
#1
# def f(s, n):
#     if s >= 25: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)
#
# print([s for s in range(1, 25) if not f(s, 1) and f(s, 2)])
# print([s for s in range(1, 25) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 25) if not f(s, 2) and f(s, 4)])


#2
# def f(s, n):
#     if s >= 1000: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 100, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)
#
# print(len([s for s in range(1, 1000) if not f(s, 1) and f(s, 2)]))
# print(len([s for s in range(1, 1000) if not f(s, 1) and f(s, 3)]))
# print([s for s in range(1, 1000) if not f(s, 2) and f(s, 4)])


#3
# def f(a, s, n):
#     if a + s >= 79: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 3, s, n - 1), f(a, s + 3, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)
#
# print([s for s in range(1, 70) if not f(9, s, 1) and f(9, s, 2)])
# print([s for s in range(1, 70) if not f(9, s, 1) and f(9, s, 3)])
# print([s for s in range(1, 70) if not f(9, s, 2) and f(9, s, 4)])


#4
# def f(s, n, p):
#     if s >= 68: return n % 2 == 0
#     if n == 0: return 0
#     if p == "":
#         h = [f(s + 1, n - 1, "+1"), f(s + 2, n - 1, "+2"), f(s * 2, n - 1, "*2")]
#     if p == "+1":
#         h = [f(s + 2, n - 1, "+2"), f(s * 2, n - 1, "*2")]
#     if p == "+2":
#         h = [f(s + 1, n - 1, "+1"), f(s * 2, n - 1, "*2")]
#     if p == "*2":
#         h = [f(s + 1, n - 1, "+1"), f(s + 2, n - 1, "+2")]
#     return any(h) if (n - 1) % 2 == 0 else all(h)
#
# print([s for s in range(1, 68) if not f(s, 1, "") and f(s, 2, "")])
# print([s for s in range(1, 68) if not f(s, 1, "") and f(s, 3, "")])
# print([s for s in range(1, 68) if not f(s, 2, "") and f(s, 4, "")])


#15
#1
# def f(a, x, y):
#     return ((x**2 - (10 * x) + 16) > 0) or ((y**2 - (10 * y) + 21) > 0) or (x * y < (2 * a))
#
# for a in range(0, 1000):
#     if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
#         print(a)
#         break


#2
# from itertools import *
#
# def f(x):
#     p = 5 <= x <= 30
#     q = 14 <= x <= 23
#     a = a1 <= x <= a2
#     return (p == q) <= (not a)
#
# ox = [i/4 for i in range(4*4, 32*4)]
# lst = []
#
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#8
#1
# from itertools import *
#
# k = 0
# for i in product("АМРТ", repeat=4):
#     k += 1
#     if k == 250:
#         print(k, i)


#2
# from itertools import *
#
# k = 1
# for i in product("АВНРЬЯ", repeat=5):
#     s = "".join(i)
#     if s[0] != "Я" and s.count("Ь") <= 1 and "ЯЯ" not in s:
#         print(k, s)
#         k += 1