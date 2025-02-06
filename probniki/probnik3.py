#2  аналитическое решение
# print("xyzw")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x or (not y)) and ((not(x == z)) and (not w))
#                 if f == 1:
#                     print(x, y, z, w)

#полное решение
# from itertools import *

# def f (x, y, z, w):
#     return (x or (not y)) and ((not(x == z)) and (not w))

# for i in product([0, 1], repeat=4):
#     table = [(0, 0, 1, i[0]), (0, i[1], 0, 1), (i[2], 1, 1, i[3])]
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
#             if len(table) == len(set(table)):
#                 print(p)


#5 алгоритм грузит не до конца
# for i in range(110000001, 1200000000):
#     N = sum(int(j) for j in str(i))
#     n = bin(N)[2:]
#     if n.count("1") % 2 == 0:
#         n = "1" + n + "00"
#     else:
#         n = "10" + n + "1"
#     r = int(n, 2)
#     if r == 21:
#         print(i)


#6
# from turtle import *
# screensize(1000000, 1000000)
# tracer(0)
# k = 50
# lt(90)

# down()
# for i in range(3):
#     lt(90)
#     for i in range(4):
#         fd(5 * k)
#         rt(90)
# up()

# for x in  range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3, "purple")
# exitonclick()


#16
from math import *

def f(n):
    return g(n -1)

def g(n):
    if n < 10: return n
    if n >= 10: return g(n - 2) + 1

c = 0
for n in range(1, 101):
    if sqrt(f(n)) % 1 == 0:
        c += 1
        print(c, sqrt(f(n)))
    