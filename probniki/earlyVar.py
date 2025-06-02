#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = x and (z <= w) and (not y)
#                 if f == 1:
#                     print(x, y, z, w)


#5
# for i in range(1, 300):
#     n = bin(i)[2:]
#     if n.count("1") % 2 == 0:
#         n = "10" + n[2:] + "0"
#     else:
#         n = "11" + n[2:] + "1"
#     r = int(n, 2)
#     if r > 480:
#         print(i)
#         break


#6
# from turtle import *
# screensize(10000, 10000)
# tracer(0)
# k = 70

# lt(90)
# down()
# rt(30)
# for i in range(3):
#     rt(150)
#     fd(6 * k)
#     rt(30)
#     fd(12 * k)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(4, "green")
# exitonclick()


#8
# from itertools import *

# lst = []
# for i in product("ДГИАШЭ", repeat=5):
#     if i[0] not in "ИАЭ" and i[-1] not in "ДГШ":
#         lst.append(i)
# print(len(lst))


#9
# c = 0
# for i in open("9-255.txt"):
#     lst = [int(x) for x in i.split()]
#     pov = [x for x in lst if lst.count(x) == 3]
#     nepov = [x for x in lst if lst.count(x) == 1]
#     if len(pov) == 6 and max(pov) > nepov[0]:
#         c += 1
# print(c)


#12
# for n in range(47, 51):
#     s = "3" + "1" * n
#     while "31" in s or "221" in s or "1111" in s:
#         if "31" in s:
#             s = s.replace("31", "1", 1)
#         if "211" in s:
#             s = s.replace("211", "13", 1)
#         if "1111" in s:
#             s = s.replace("1111", "2", 1)
#     lst = sum(int(x) for x in s)
#     print(n, lst)


#13
# from ipaddress import *

# net = ip_network("143.168.72.213/255.255.255.240", 0)
# for i in net:
#     print(i)


#14
# for x in "0123456789abcdefghijk":
#     n = int(f"82934{x}2", 21) + int(f"2924{x}{x}7", 21) + int(f"67564{x}8", 21)
#     if n % 20 == 0:
#         print(n // 20)
#         break
    
    
#15
# def f(a, x, y):
#     return (5 < y) or (x > 32) or (x + 2 * y < a)

# for a in range(0, 1000):
#     if all(f(a, x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break


#16
# from sys import *
# setrecursionlimit(10000)

# def f(n):
#     if n <= 5: return 1
#     if n > 5: return n + f(n - 2)

# print(f(2126) - f(2122))


#17
# f = open("probniki\\17-432.txt")
# lst = [int(x) for x in f]
# su_n = sum(x for x in lst if x < 0)

# ans = []
# for i in range(1, len(lst) - 1):
#     a = [lst[i - 1], lst[i], lst[i + 1]]
#     if max(a) * min(a) > su_n:
#         ans.append(sum(a))
# print(len(ans), abs(max(ans)))


#19-21
# def f(s, n):
#     if s <= 87: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s - 2, n - 1), f(s // 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(88, 300) if f(s, 2)])
# print([s for s in range(88, 300) if not f(s, 1) and f(s, 3)])
# print([s for s in range(88, 300) if not f(s, 2) and f(s, 4)])


#23
# def f(x, y):
#     if x == y: return 1
#     if x > y or x == 35: return 0
#     else: return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
    
# print(f(7, 13) * f(13, 15) * f(15, 51))