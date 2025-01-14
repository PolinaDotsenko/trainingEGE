#12     +
# for i in range(101, 500):
#     s = i * "5"
#     while "555" in s or "11" in s or "2" in s:
#         if "555" in s:
#             s = s.replace("555", "1", 1)
#         if "11" in s:
#             s = s.replace("11", "25", 1)
#         if "2" in s:
#             s = s.replace("2", "5", 1)
#     if s == "15": print(i)


#14     +
# n = 4 * 625**1920 + 4 * 125**1930 - 4 * 25**1940 - 3 * 5**1950 - 1960
# base = 5
# lst = []
# while n > 0:
#     lst.append(n % base)
#     n = n // base
# print(lst[::-1].count(0))


#15     +
# def f(a, x, y):
#     return (x + 2 * y > a) or (y < x) or (x < 30)

# for a in range(0, 300):
#     if all(f(a, x, y) for x in range(0, 300) for y in range(0, 300)):
#         print(a)


#16     +
# def f(n):
#     if n >= 2022: return n
#     if n < 2022: return f(n + 5) + 7
# print(f(45) - f(49))


#25     на проверке
# from fnmatch import *

# for i in range(4013, 10**12 + 1, 4013):
#     if fnmatch(str(i), "123?4*5679"):
#         print(i, i // 4013)

    
#теория игр
# def f(a, s, n):
#     if a >= 50 or s >= 50: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 3, s, n - 1), f(a, s + 3, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(0, 28) if f(22, s, 2)])       +
# print([s for s in range(0, 28) if not f(22, s, 1) and f(22, s, 3)])       +
# print([s for s in range(0, 28) if not f(22, s, 2) or f(22, s, 4)])        -


#5 +
# for i in range(0, 100):
#     n = str(bin(i)[2:])
#     s = sum([int(i) for i in n])
#     m = str(n[-2:])
#     if s % 2 == 0:
#         l = n + m
#     else:
#         l = n + m[::-1]
#     r = int(l, 2)
#     if r > 154:
#         print(i)


#7 +
# v = 1024000 * 5
# t = v / (16 * 32 * 1000 * 1)
# print(t)


#10 +
#1 +
#4 +