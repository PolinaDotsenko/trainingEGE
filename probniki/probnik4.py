#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(x, y, z, w)


#8
# from itertools import *

# lst = []
# for i in product(range(12), repeat=5):
#     if i[0] != 0 and i.count(7) == 1 and sorted(i)[-4] <= 8:
#         lst.append(i)
# print(len(lst))


#6
# from turtle import *


# screensize(100000, 100000)
# tracer(0)
# k = 30

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
#         dot(3, "pink")
# exitonclick()

# print((12 + 4) * 2)


#12
# s = "9" * 81

# while "33333" in s or "999" in s:
#     if "33333" in s:
#         s = s.replace("33333", "99", 1)
#     else:
#         s = s.replace("999", "3")
# print(s)


#16
# from sys import *


# setrecursionlimit(1000000000)
# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n - 1) * f(n -1)
# print((f(2024) + (2 * f(2023))) / f(2022))

#1
#4



5...