#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#16
# def f(n):
#     if n >= 1300: return n
#     if n < 1300 and n % 2 != 0: return n * f(n + 1)
#     if n < 1300 and n % 2 == 0: return (n * f(n + 2)) / 4
# print(f(1286) / f(1290))


#6
# from turtle import *
# screensize(100000, 10000)
# tracer(0)
# k = 50
#
# down()
# lt(90)
# for i in range(4):
#     fd(3 * k * 4)
#     rt(90)
# up()
# fd(4 * k)
# rt(90)
# fd(4 * k)
# down()
# for i in range(4):
#     fd(4 * k)
#     lt(90)
# up()
#
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3, "red")
# exitonclick()


#23
# def f(x, y):
#     if x == y: return 1
#     if x > y or x == 15 or x == 35: return 0
#     else:
#         return f(x + 1, y) + f(x * 2, y) + f(x**2, y)
# print(f(2, 20) * f(20, 60) * f(60, 100))


#17
# f = open("17-404.txt")
# lst = [int(x) for x in f]
# m = min(lst)
#
# res = []
# for i in range(0, len(lst) - 1):
#     a, b = lst[i], lst[i + 1]
#     if a % 55 == m or b % 55 == m:
#         res.append(a + b)
# print(len(res), min(res))


#

























