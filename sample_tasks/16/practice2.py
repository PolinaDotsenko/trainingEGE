#1
# def f(n):
#     if n <= 1: return 1 
#     if n % 2 == 0 and n > 1:
#         return n + f(n - 1)
#     if n % 2 != 0 and n > 1: 
#         return n * n + f(n - 2)
# print(f(80))


#2
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 2 * f(n - 1) + n + 3
# print(f(19))


#3
# def f(n):
#     if n < 5: return 5 - n
#     if n >= 5 and n % 3 == 0: return 4 * (n - 5) * f(n - 5)
#     if n >= 5 and n % 3 != 0: return 3 * n + 2 * f(n - 1) + f(n - 2)
# print(f(20))


#4
# def f(n):
#     if n <= 3: return n
#     if n % 2 == 0 and n > 3: return 2 * n + f(n - 1)
#     if n % 2 != 0 and n > 3: return n * n + f(n - 2)
    
# c = 0
# for n in range(1, 101):
#     if f(n) % 3 == 0:
#         c += 1
# print(c)


#5
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + 3 * g(n - 1)

# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)

# res = sum([int(x) for x in str(f(18))])
# print(res)


#6
# from functools import *

# @lru_cache(None)
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - 2 * g(n - 1)
    
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + g(n - 1) + n

# res = sum([int(x) for x in str(g(36))])
# print(res)


#7
# def f(n):
#     if n < 2: return 1
#     if n >= 2 and n % 2 == 0: return f(n / 2) + 1
#     if n >= 2 and n % 2 != 0: return f(n - 3) + 3
    
# c = 0
# for n in range(1, 10001):
#     if f(n) == 12:
#         c += 1
# print(c)


#8
# from sys import *
# setrecursionlimit(10000)

# def f(n):
#     if n < 3: return 3
#     if n >= 3: return 2 * n + 5 + f(n - 2)
# print(f(3027) - f(3023))


#9
# from sys import *
# from functools import *
# setrecursionlimit(10**9)
# @lru_cache(None)

# def f(n):
#     if n > 10000: return n - 10000
#     if 1 <= n <= 10000: return f(n + 1) + f(n + 2)
# print(f(12345) * (f(10) - f(12)) / f(11) + f(10101))