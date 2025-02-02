#2
# from itertools import *

# def f(x, y, z, w):
#     return w and ((y <= x) <= z)

# for i in product([0, 1], repeat=5):
#     table = [(i[0], i[1], 0, 1), (0, i[2], i[3], 0), (0, 1, i[4], 1)]
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p, r))) for r in table] == [1, 1, 0]:
#             print(p)


#2 hw
# from itertools import * 

# def f(x, y, z, w):
#     return (x == (w or y)) or ((w <= z) and (y <= w))

# for i in product([0,1], repeat=7):
#     table = [(1, i[0], i[1], 1), (i[2], i[3], i[4], 1), (1, i[5], 1, i[6])]
#     for p in permutations("xyzw"):
#         if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
#             print(p)


#5
# for i in range(0, 1000):
#     n = bin(i)[2:]
#     n += str(n.count("1") % 2)
#     n += str(n.count("1") % 2)
#     r = int(n, 2)
#     if r > 150:
#         print(r)
#         break


#5 hw
# ans = []
# for i in range(1, 500):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n = "1" + n + "0"
#     if i % 2 != 0:
#         n = "11" + n + "11"
#     r = int(n, 2)
#     if r > 52:
#         ans.append(i)
# print(min(ans))


#6
# from turtle import * 

# screensize(10000, 10000)
# tracer(0)
# k = 20
# lt(90)

# backward(4 * k)
# down()
# for i in range(8):
#     fd(12 * k)
#     rt(45)
#     fd(7 * k)
#     rt(45)
#     fd(6 * k)
#     rt(90)
# up()

# for x in range(1, 50):
#     for y in range(1, 50):
#         goto(x * k, y * k)
#         dot(5, "red")
# exitonclick()


#6 hw
# from turtle import *

# screensize(10000, 10000)
# tracer(0)
# k = 25
# lt(90)

# down()
# for i in range(4):
#     fd(10 * k)
#     rt(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(3, "pink")
# exitonclick()


#8
# from itertools import *

# c = 0
# for i in product("012345678", repeat=6):
#     s = "".join(i)
#     if s[0] not in "01357" and s[-1] not in "23" \
#         and s.count("1") >= 2:
#         c += 1
# print(c)


#9
# c = 1
# for i in open("probniki\\janWeb\\9.txt"):
#     lst = [int(x) for x in i.split()]
#     pov = [x for x in lst if lst.count(x) == 3]
#     nepov = [x for x in lst if lst.count(x) == 1]
#     if len(pov) == 6 and sum(pov) / len(pov) < nepov[0]:
#         print(c)
#     c += 1
    

#12
# for i in range(81, 100):
#     s = "1" * i
#     while "111" in s:
#         s = s.replace("111", "2", 1)
#         s = s.replace("2222", "1", 1)
#     if s.count("1") < 1:
#         print(i, s)


#13
# from ipaddress import *

# for mask in range(33): #единиц может быть от 0 до 32
#     net = ip_network(f"90.155.69.100/{mask}", 0)
#     print(net, net.netmask)


#14
# def f(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# n = (7**(9**2 - 1) - (10 - 3)**4) * (5/6) * 8

# print(f(n, 7).count(4))


#15
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(a, 9) and (d(280, x) <= ((not d(a, x)) <= (not d(730, x))))

# c = 0
# for a in range(1, 1001):
#     if all(f(a, x) for x in range(1, 500)):
#         c += 1
#         print(a, c)


#16
# def f(n):
#     if n < 3: return n + 3
#     if n >= 3 and n % 3 == 0: return (n + 2) * f(n - 4)
#     if n >= 2 and n % 3 != 0: return n + f(n - 1) + 2 * f(n - 2)
# print(f(20))


#17
# f = open("probniki\\janWeb\\17-1.txt")
# lst = [int(x) for x in f]
# c = 0
# last = 0
# mdist = 10**6
# for i in range(1, len(lst) - 1):
#     if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
#         c += 1
#         mdist = min(mdist, i - last)
#         last = i
# print(c, mdist)