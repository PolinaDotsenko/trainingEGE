#1
# def f(n):
#     if n <= 1: return 1
#     if n > 1 and n % 2 == 0: return n + f(n - 1)
#     if n > 1 and n % 2 != 0: return n * n + f(n - 2)
# print(f(82))


#2
# def f(n):
#     if n <= 1: return 1
#     if n > 1 and n % 2 == 0: return n * f(n - 1)
#     if n > 1 and n % 2 != 0: return n + f(n - 2)
# print(f(84))


#3 с условием на определенном отрезке
# def f(n):
#     if n <= 3: return n
#     if n > 3 and n % 2 == 0: return 2 * n + f(n - 1)
#     if n > 3 and n % 2 != 0: return n * n + f(n - 2)

# lst = [f(x) for x in range(1, 101) if f(x) % 3 == 0]
# print(len(lst))


#4
# def f(n):
#     if n <= 10: return n
#     if 10 < n <= 36: return n // 4 + f(n - 10)
#     if n > 36: return 2 * f(n - 5)
# print(f(100))


#5
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + 3 * g(n - 1)

# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)

# s = sum([int(x) for x in str(f(18))])
# print(s)


#6 !!!!!
# from functools import *

# @lru_cache  #ставится перед функцией
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)

# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + g(n - 1) + n

# s = sum([int(x) for x in str(g(36))])
# print(s)


#7
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 2 == 0: return f(n / 2) + 1
#     if n >= 2 and n % 2 != 0: return f(n - 3) + 3

# s = len([f(x) for x in range(1, 10001) if f(x) == 12])
# print(s)


#8
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 3 == 0: return f(n / 3) + 1
#     if n >= 2 and n % 3 != 0: return f(n - 2) + 5

# for n in range(2, 10000):
#     if f(n) == 73:
#         print(n)
#         break


#9 доп номера
# from sys import *
# setrecursionlimit(1000000000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return (3 * n + 5) * f(n - 1)

# print(f(2073) / f(2070))


#10
# from sys import *
# setrecursionlimit(1000000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return n + f(n - 1)

# c = 0
# for n in range(1, 101):
#     if f(2023) // f(n) % 2 == 0:
#         c += 1
# print(c)