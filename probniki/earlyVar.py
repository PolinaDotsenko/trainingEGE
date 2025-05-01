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