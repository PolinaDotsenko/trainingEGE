#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
            
#             for w in 0, 1:
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(x, y, z, w)


#23
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     else:
#         return f(x - 2, y) + f(x % 2, y)
    
# print(f(38, 16) * f(16, 2))


#6
# from turtle import *

# screensize(10000, 10000)
# tracer(0)
# k = 25

# lt(90)
# down()
# for i in range(9):
#     fd(12 * k)
#     rt(90)
#     fd(6 * k)
#     rt(90)
# up()
# fd(k)
# rt(90)
# fd(3 * k)
# lt(90)
# down()
# for i in range(9):
#     fd(53 * k)
#     rt(90)
#     fd(75 * k)
#     rt(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3, "green")
# exitonclick()


#5
# for i in range(1, 500):
#     n = bin(i)[2:]
#     n = n + str(n.count("1") % 2)
#     n = n + str(n.count("1") % 2)
#     r = int(n, 2)
#     if r > 123:
#         print(r)
#         break


#8
# from itertools import *

# res = 0
# for i in product(range(12), repeat=5):
#     if i[0] != 0 and i.count(7) == 1 and (i.count(9) + i.count(10) + i.count(11)) <= 3:
#         res += 1
# print(res)


#12
# s = "9" * 81
# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace("33333", "99", 1)
#     else:
#         s = s.replace("999", "3", 1)
# print(s)


#16
# from sys import *
# setrecursionlimit(10000000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n - 1) * f(n - 1)
# print((f(2024) + 2 * f(2023)) / f(2022))


#15
# def f(a, x, y):
#     return (x + y <= 30) or (y <= x + 2) or (y >= a)

# for a in range(900, 1000):
#     if all([f(a, x, y) == 1 for x in range(900, 1000) for y in range(900, 1000)]):
#         print(a)


#14
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# for x in range(1, 90000):
#     n = 3**2000 + 3**10 - x
#     if convert(n, 3).count(2) >= 2000:
#         print(x)
#         break


#25
# from fnmatch import *

# for i in range(1917, 10**10 + 1, 1917):
#     if fnmatch(str(i), "3?12?14*5"):
#         print(i, i // 1917)


#19-21
# def f(s, n):
#     if s <= 19: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s - 2, n - 1), f(s - 5, n - 1), f(s // 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(20, 300) if f(s, 2)])
# print([s for s in range(20, 300) if not f(s, 1) and f(s, 3)])
# print([s for s in range(20, 300) if not f(s, 2) and f(s, 4)])


#9
# c = 0
# for i in open("probniki\\9-247.txt"):
#     lst = sorted([int(x) for x in i.split()])
#     s = set(lst)
#     if list(s) == lst:
#         if max(lst) + min(lst) > lst[1] + lst[2]:
#             c += 1
# print(c)


#13
# from ipaddress import *

# c = 0
# net = ip_network("172.16.168.0/255.255.248.0", 0)
# for i in net:
#     s = str(i).split(".")
#     lst = [int(x) for x in s]
#     b = "".join([bin(j)[2:] for j in lst])
#     if b.count("1") % 5 != 0:
#         c += 1
# print(c)