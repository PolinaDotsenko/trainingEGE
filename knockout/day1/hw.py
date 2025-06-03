#1
# from sys import *
# from functools import *
# setrecursionlimit(1000000)
# @lru_cache(maxsize=None)
# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 2 == 0: return f(n // 10) + (n % 10)
#     if n % 2 != 0: return f(n // 10)
#
# res = 0
# for k in range(10**9, 10**9 * 2 + 1):
#     if f(k) == 2:
#         res += 1
# print(res)


#2
# def f(n):
#     if n == 0: return 0
#     if n % 3 == 0 and n > 0: return n + f(n - 3)
#     if n % 3 > 0: return n + f(n - (n % 3))
# print(f(26))


#3
# def f(n):
#     if n <= 2: return 1
#     if n > 2: return f(n - 1) + 3 * f(n - 2)
# print(f(7))


#4
# from sys import *
# setrecursionlimit(1000000)
#
# def f(n):
#     if n < 11: return 10
#     if n >= 11: return n + f(n - 1)
# print(f(2204) - f(2202))


#5
# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 2 == 0: return f(n / 2)
#     if n % 2 != 0: return 1 + f(n - 1)
#
# res = 0
# for n in range(1, 501):
#     if f(n) == 3:
#         res += 1
# print(res)


#6
# from functools import *
# from sys import *
# setrecursionlimit(10**9)
#
# @lru_cache(maxsize=None)
# def f(a, b):
#     if b == 0: return a
#     if a >= b > 0: return f(a - b, b)
#     if a < b: return f(b, a)
#
# res = 0
# for n in range(123456798, 1234567886):
#     if f(n, 15) == 1:
#         res += 1
# print(res)


#7
# def f(n):
#     if n <= 2: return 2
#     if n > 2: return f(n - 1) * f(n - 2)
# print(f(5))


#8
# def f(n):
#     if n == 0: return 0
#     if n % 3 == 0 and n > 0: return n + f(n - 3)
#     if n % 3 > 0: return n + f(n - (n % 3))
# print(f(22))


#9
# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 3 == 0: return f(n / 3)
#     if n % 3 > 0: return (n % 3) + f(n - (n % 3))
#
# for i in range(0, 1000):
#     if f(i) == 9:
#         print(i)
#         break


#1
# f = open("17.txt")
# lst = [int(x) for x in f]
# end3 = [x for x in lst if abs(x) % 10 == 3]
# res = []
#
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if a % 10 == b % 10:
#         if (a % 3 == 0 and b % 3 != 0) or (b % 3 == 0 and a % 3 != 0):
#             if a**2 + b**2 <= min(end3)**2:
#                 res.append(a**2 + b**2)
# print(len(res), max(res))


#2
# f = open("17.txt")
# lst = [int(x) for x in f]
# end3 = [x for x in lst if abs(x) % 10 == 3]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (abs(a) % 10 == 3 and abs(b) % 10 != 3) or (abs(b) % 10 == 3 and abs(a) % 10 != 3):
#         if a**2 + b**2 >= max(end3)**2:
#             res.append(a**2 + b**2)
# print(len(res), max(res))


#3
# f = open("17.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a + b) % 8 == 0:
#         res.append(a + b)
# print(len(res), max(res))


#4
# f = open("17.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if ((a - b) % 2 == 0) and (a % 31 == 0 or b % 31 == 0):
#         res.append(a + b)
# print(len(res), max(res))


#5
# f = open("17.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a * b) % 14 != 0:
#         res.append(a + b)
# print(len(res), max(res))


#6
# f = open("1_17.txt")
# lst = [int(x) for x in f]
# end17 = [x for x in lst if abs(x) % 100 == 17]
# res = []
# for i in range(0, len(lst) - 2):
#     a, b, c = lst[i], lst[i + 1], lst[i + 2]
#     if ((99 < abs(a) < 1000) and (abs(b) > 999 or abs(b) < 100) and (abs(c) > 999 or abs(c) < 100)) \
#         or ((99 < abs(b) < 1000) and (abs(a) > 999 or abs(a) < 100) and (abs(c) > 999 or abs(c) < 100)) \
#             or ((99 < abs(c) < 1000) and (abs(a) > 999 or abs(a) < 100) and (abs(b) > 999 or abs(b) < 100)):
#         if a + b + c < max(end17):
#             res.append(a + b + c)
# print(len(res))


#7
# f = open("17.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a + b) % 10 == 0:
#         res.append(a + b)
# print(len(res), max(res))


#8
# f = open("17.txt")
# lst = [int(x) for x in f]
# end7 = [x for x in lst if x % 10 == 7]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (abs(a) % 10 == 7 and abs(b) % 10 != 7) or (abs(b) % 10 == 7 and abs(a) % 10 != 7):
#         if (a**2 + b**2) < min(end7)**2:
#             res.append(a**2 + b**2)
# print(len(res), max(res))


#9
# f = open("17.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if (a % 5 == 0 or b % 5 == 0) and (a + b) % 7 == 0:
#         res.append(a + b)
# print(len(res), max(res))