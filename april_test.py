#1
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (d(x, 2) <= (not d(x, 5))) or (x + a >= 70)

# for a in range(1, 1000):
#     if all(f(a, x) == 1 for x in range(1, 1000)):
#         print(a)
#         break


#2????
# from itertools import *

# def f(x):
#     p = 5 <= x <= 10
#     q = 10 <= x <= 20
#     r = 25 <= x <= 40
#     a = a1 <= x <= a2
#     return a <= p == q <= r

# lst = []
# ox = [i / 4 for i in range(4*4, 42*4)]
# for a1, a2 in combinations(ox, 2):
#     if any(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#3
# from functools import *

# @lru_cache(None)            #!@@@@@@@@@@@@@@@@@@@
# def f(n):
#     if n == 0: return 0
#     if 1 <= n < 3: return 1
#     if n >= 3: return f(n - 1) + f(n - 2)
# print(f(47))


#4
# def f(n):
#     if n == 1: return 1
#     if n > 1: return 2 * f(n - 1) + g(n - 1) - 2 * n
    
# def g(n):
#     if n == 1: return 1
#     if n > 1: return f(n - 1) + 2 * g(n - 1) + n
    
# print(f(14) + g(14))


#5??????
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# for x in range(5001, 8000):
#     res = convert(7100 - x, 7)
#     if res.count(0) == 5:
#         print(x)


#6
# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# k = 50

# lt(90)
# down()
# rt(45)
# for i in range(9):
#     fd(9 * k)
#     rt(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(4, "blue")
# exitonclick()


#8
# def f(a, s, n):
#     if a + s >= 65: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(2, 58) if f(6, s, 2)])
# print([s for s in range(2, 58) if not f(6, s, 1) and f(6, s, 3)])
# print([s for s in range(2, 58) if not f(6, s, 2) and f(6, s, 4)])


#9
# def f(s, n):
#     if s >= 165: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 1, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 165) if f(s, 2)])
# print([s for s in range(1, 165) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 165) if not f(s, 2) and f(s, 4)])
