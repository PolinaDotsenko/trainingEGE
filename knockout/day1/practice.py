#17 старые
#1
# c = 0
# for i in range(3439, 7411):
#     if i % 9 == 0 or i % 10 == 0 or i % 11 == 0:
#         if i % 2 != i % 6:
#             c += 1
# print(c)

#2
# lst = []
# for i in range(3**7, 3**8):
#     if i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
#         lst.append(i)
# print(sum(lst))


#3
# lst = []
# for i in range(2738, 7515):
#     if i % 7 == 0 and i % 19 != 0:
#         lst.append(i)
# print(len(lst), sum(lst))


#17 актуальные
#1
# res = []
# f = open("17-1.txt")
# lst = [int(x) for x in f]
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if a % 3 == 0 or b % 3 == 0:
#         res.append(a + b)
# print(len(res), max(res))


#2
# f = open("17-1.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if (str(a)[-1] == "6" and a % 3 == 0) or (str(b)[-1] == "6" and b % 3 == 0):
#         res.append(min(a, b))
# print(len(res), min(res))


#3
# f = open("17-2.txt")
# lst = [int(x) for x in f]
# print(lst.count(max(lst)), lst.index(max(lst)) + 1)


#4
# f = open("17-4.txt")
# lst = [int(x) for x in f]
# avr = sum(lst) / len(lst)
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if a < avr and b < avr and (str(a)[-1] == "9" or str(b)[-1] == "9"):
#         res.append(a + b)
# print(len(res), max(res))


#5 досрок
# f = open("17-432.txt")
# lst = [int(x) for x in f]
# n = sum(x for x in lst if x < 0)
# res = []
# for i in range(0, len(lst) - 2):
#     a, b, c = lst[i], lst[i+1], lst[i+2]
#     if min(a, b, c) * max(a, b, c) > n:
#         res.append(a + b + c)
# print(len(res), abs(max(res)))


#6
# f = open("17-426.txt")
# lst = [int(x) for x in f]
# res = []
# n = max(x for x in lst if 10000 < x > 9999 and x % 100 == 43)
# for i in range(0, len(lst) - 2):
#     a, b, c = lst[i], lst[i+1], lst[i+2]
#     if (10000 < abs(a) > 9999 and abs(a) % 100 == 43) \
#             or (10000 < abs(b) > 9999 and abs(b) % 100 == 43) or (10000 < abs(c) > 9999 and abs(c) % 100 == 43):
#         if a**2 + b**2 + c**2 <= n**2:
#             res.append(a**2 + b**2 + c**2)
# print(len(res), min(res))


#7
# f = open("17-403.txt")
# lst = [int(x) for x in f]
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i+1]
#     if (a % 77) * (b % 77) == min(lst)**2:
#         res.append(a * b)
# print(len(res), min(res))


#16
#1
# def f(n):
#     if n <= 1: return 1
#     if n % 2 == 0 and n > 1: return n + f(n - 1)
#     if n % 2 != 0 and n > 1: return n * n + f(n - 2)
# print(f(82))


#2
# def f(n):
#     if n <= 1: return 1
#     if n % 2 == 0 and n > 1: return n * f(n - 1)
#     if n % 2 != 0 and n > 1: return n + f(n - 2)
# print(f(84))


#3
# def f(n):
#     if n <= 3: return n
#     if n % 2 == 0: return 2 * n + f(n - 1)
#     if n % 2 != 0: return n * n + f(n - 2)
#
# res = 0
# for i in range(1, 101):
#     if f(i) % 3 == 0:
#         res += 1
# print(res)


#4
# def f(n):
#     if n <= 10: return n
#     if 10 < n <= 36: return n // 4 + f(n - 10)
#     if n > 36: return 2 * f(n - 5)
# print(f(100))


#5
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + (3 * g(n - 1))
#
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - (2 * g(n - 1))
#
# print(f(18)) #потом найти сумму цифр значения


#6
# from functools import *
#
# @lru_cache(maxsize=None)
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - (2 * g(n - 1))
#
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + g(n - 1) + n
#
# print(g(36)) #найти сумму цифр значения


#7
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 2 == 0: return f(n / 2) + 1
#     if n >= 2 and n % 2 != 0: return f(n - 3) + 3
#
# res = 0
# for i in range(1, 10001):
#     if f(i) == 12:
#         res += 1
# print(res)


#8
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 3 == 0: return f(n / 3) + 1
#     if n >= 2 and n % 3 != 0: return f(n - 2) + 5
#
# for i in range(2, 10000):
#     if f(i) == 73:
#         print(i)
#         break


#9
from sys import *
setrecursionlimit(1000000)

def f(n):
    if n <= 5: return 1
    if n > 5: return n + f(n - 2)
print(f(2126) - f(2122))