#1
# def f(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) - g(n - 1)
    
# def g(n):
#     if n == 1: return 1
#     if n >= 2: return f(n - 1) + g(n - 1)

# print(f(5) / g(5))


#2
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 5 * f(n - 1) + 3 * n
# print(f(4))


#3
# from sys import *
# setrecursionlimit(10000)

# def f(n):
#     if n < 11: return 10
#     if n >= 11: return n + f(n - 1)
# print(f(2024) - f(2022))


#4
# def f(n):
#     if n <= 2: return n + 1
#     if n > 2: return f(n - 1) * f(n - 2)
# print(f(4))


#5
# def f(n):
#     if n == 1: return 1
#     if n > 1: return f(n - 1) + n
# print(f(40))


#6
# def f(n):
#     if n == 0: return 0
#     if n > 0 and n % 2 == 0: return f(n / 2)
#     if n % 2 != 0: return 1 + f(n - 1)

# c = 0 
# for n in range(1, 1001):
#     if f(n) == 3:
#         c += 1
# print(c)


#7
# def f(n):
#     if n <= 2: return n
#     if n > 2: return f(n - 1) + 2 * f(n - 2)
# print(f(6))